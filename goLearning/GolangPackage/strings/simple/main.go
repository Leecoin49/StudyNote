package main

import (
	"fmt"
	"strings"
)

func main() {
    // 原始石碑
    raw := "  Go is Awesome!  "

    // 1. 清洗：去掉首尾空格 (Trim)
    clean := strings.TrimSpace(raw) 
    
    // 2. 检查：这是不是我们想要的？ (Prefix/Suffix/Contains)
    if strings.HasPrefix(clean, "Go") {
        fmt.Println("Found Go!")
    }

    // 3. 改造：生成新副本 (Replace/ToUpper)
    // 注意：raw 本身并没有变！shouting 是个新字符串
    shouting := strings.ToUpper(clean) 

    // 4. 分割：拆成碎片 (Split)
    parts := strings.Split(clean, " ")

    fmt.Printf("Original: [%s]\n", raw) // 原件完好无损
    fmt.Printf("Clean:    [%s]\n", clean)
    fmt.Printf("Shouting: [%s]\n", shouting)
    fmt.Printf("Parts:    %v\n", parts)
}