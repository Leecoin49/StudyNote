package main

import (
	"image"
	"image/color"
	"image/gif"
	"io"
	"math"
	"math/rand"
	"os"
	"time"
)

// 1. 修改调色板：
// 索引 0 是黑色（背景），后续索引是彩虹色序列
var palette = []color.Color{
	color.Black,                        // 0: 背景色
	color.RGBA{0xff, 0x00, 0x00, 0xff}, // 1: 红色
	color.RGBA{0x00, 0xff, 0x00, 0xff}, // 2: 绿色
	color.RGBA{0x00, 0x00, 0xff, 0xff}, // 3: 蓝色
	color.RGBA{0xff, 0xff, 0x00, 0xff}, // 4: 黄色
	color.RGBA{0x00, 0xff, 0xff, 0xff}, // 5: 青色
	color.RGBA{0xff, 0x00, 0xff, 0xff}, // 6: 洋红
}

func main() {
	// 设置随机数种子，确保每次运行图形不同
	rand.Seed(time.Now().UnixNano())

	file, err := os.Create("lissajous_color.gif")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	lissajous(file)
}

func lissajous(out io.Writer) {
	const (
		cycles  = 5     // 振荡器完整旋转的次数
		res     = 0.001 // 角度分辨率
		size    = 100   // 画布大小 [-size..+size]
		nframes = 64    // 动画帧数
		delay   = 8     // 帧延迟（以10ms为单位）
	)

	freq := rand.Float64() * 3.0 // y振荡器的相对频率
	anim := gif.GIF{LoopCount: nframes}
	phase := 0.0 // 相位差

	for i := 0; i < nframes; i++ {
		rect := image.Rect(0, 0, 2*size+1, 2*size+1)
		img := image.NewPaletted(rect, palette)

		for t := 0.0; t < cycles*2*math.Pi; t += res {
			x := math.Sin(t)
			y := math.Sin(t*freq + phase)

			// 2. 修改 SetColorIndex 的第三个参数：
			// 我们利用 t 的变化来改变颜色。
			// len(palette)-1 是因为我们要排除掉索引0（背景色）。
			// +1 是为了确保我们取到的索引是 1 到 6（即具体的颜色）。
			colorIndex := uint8(int(t)%(len(palette)-1) + 1)

			img.SetColorIndex(size+int(x*size+0.5), size+int(y*size+0.5), colorIndex)
		}

		phase += 0.1
		anim.Delay = append(anim.Delay, delay)
		anim.Image = append(anim.Image, img)
	}
	gif.EncodeAll(out, &anim) // 注意：忽略了编码错误
}