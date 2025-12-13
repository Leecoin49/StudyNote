package main

import (
	"fmt"
	"strings"
	"time"
)

func main() {
	// ==========================================
	// 1. 准备数据
	// ==========================================
	// 我们生成 50,000 个字符串放入切片中模拟 os.Args
	// 数据量必须够大，否则差异太小看不出来
	dataSize := 50000
	testData := make([]string, dataSize)
	for i := 0; i < dataSize; i++ {
		testData[i] = "test"
	}
	fmt.Printf("正在测试拼接 %d 个字符串...\n\n", dataSize)

	// ==========================================
	// 2. 测量低效版本 (+=)
	// ==========================================
	start1 := time.Now() // 记录开始时间

	s1, sep := "", ""
	for _, arg := range testData {
		s1 += sep + arg
		sep = " "
	}

	duration1 := time.Since(start1) // 计算耗时
	fmt.Printf("低效版本 (+=) 耗时: %v\n", duration1)

	// ==========================================
	// 3. 测量高效版本 (strings.Join)
	// ==========================================
	start2 := time.Now() // 记录开始时间

	s2 := strings.Join(testData, " ")

	duration2 := time.Since(start2) // 计算耗时
	fmt.Printf("高效版本 (Join) 耗时: %v\n", duration2)

	// ==========================================
	// 4. 验证结果 (确保两个逻辑输出一致)
	// ==========================================
	if s1 == s2 {
		fmt.Println("\n结果验证: 内容一致")
	} else {
		fmt.Println("\n结果验证: 内容不一致!")
	}
    
    // 计算倍数差异
    if duration2 > 0 {
        fmt.Printf("性能差异: strings.Join 比 += 快了约 %.2f 倍\n", float64(duration1)/float64(duration2))
    }
}