package main

import (
    "fmt"
    "unicode/utf8"
)

func main() {
    // 一个包含英文、中文和 Emoji 的字符串
    // 'Hello' (5 bytes) + '世界' (6 bytes) + '👋' (4 bytes)
    s := "Hello世界👋"

    // ❌ 错误做法：直接看长度
    fmt.Printf("len(s): %d\n", len(s)) // 输出 15 (是字节数！)

    // ❌ 错误做法：普通的 for 循环
    // 这会按字节遍历，中文会被拆碎
    fmt.Printf("Byte traversal: ")
    for i := 0; i < len(s); i++ {
        fmt.Printf("%x ", s[i]) 
    }
    fmt.Println()

    // ✅ 正确做法 1：统计字符数量
    runeCount := utf8.RuneCountInString(s)
    fmt.Printf("Rune count: %d\n", runeCount) // 输出 7 (5+2+1)

    // ✅ 正确做法 2：range 遍历 (Go 的 range 对字符串有特殊优化)
    // 它会自动按照 Rune (Unicode 码点) 进行解码
    fmt.Printf("Rune traversal: ")
    for idx, r := range s {
        // idx 是当前字符起始的字节位置，r 是字符本身
        fmt.Printf("(%d: %c) ", idx, r)
    }
    fmt.Println()

    // ✅ 正确做法 3：如何安全截取前 N 个字符？
    // 先转成 []rune 切片 (注意：这会产生内存分配)
    runes := []rune(s)
    if len(runes) >= 7 {
        sub := string(runes[5:7]) // 截取 "世界"
        fmt.Printf("Substring: %s\n", sub)
    }
}