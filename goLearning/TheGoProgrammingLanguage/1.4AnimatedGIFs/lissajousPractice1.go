// // Lissajous generates GIF animations of random Lissajous figures.
// package main

// import (
//     "image"
//     "image/color"
//     "image/gif"
//     "io"
//     "math"
//     "math/rand"
//     "os"
// )

// var palette = []color.Color{color.White, color.RGBA{0x00, 0xFF, 0x00, 0xff}}

// const (
//     whiteIndex = 0 // first color in palette
//     blackIndex = 1 // next color in palette
// )

// func main() {
//     // 创建一个文件用于写入 GIF 数据
//     file, err := os.Create("./lissajous.gif")
//     if err != nil {
//         panic(err) // 如果创建文件失败，程序将终止并打印错误
//     }
//     defer file.Close() // 确保在函数结束时关闭文件

//     // 调用 lissajous 函数，并将结果写入文件
//     lissajous(file)
// }

// func lissajous(out io.Writer) {
//     const (
//         cycles  = 5     // number of complete x oscillator revolutions
//         res     = 0.001 // angular resolution
//         size    = 100   // image canvas covers [-size..+size]
//         nframes = 64    // number of animation frames
//         delay   = 8     // delay between frames in 10ms units
//     )

//     freq := rand.Float64() * 3.0 // relative frequency of y oscillator
//     anim := gif.GIF{LoopCount: nframes}
//     phase := 0.0 // phase difference
//     for i := 0; i < nframes; i++ {
//         rect := image.Rect(0, 0, 2*size+1, 2*size+1)
//         img := image.NewPaletted(rect, palette)
//         for t := 0.0; t < cycles*2*math.Pi; t += res {
//             x := math.Sin(t)
//             y := math.Sin(t*freq + phase)
//             img.SetColorIndex(size+int(x*size+0.5), size+int(y*size+0.5),
//                 blackIndex)
//         }
//         phase += 0.1
//         anim.Delay = append(anim.Delay, delay)
//         anim.Image = append(anim.Image, img)
//     }
//     gif.EncodeAll(out, &anim) // NOTE: ignoring encoding errors
// }