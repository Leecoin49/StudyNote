package main

import (
	"fmt"
	"strings"
)

// GenerateSQL 模拟构建一个批量插入的 SQL 语句
// 场景：我们需要拼接 INSERT INTO users (name, age) VALUES ('A', 1), ('B', 2)...
func GenerateSQL(users []string) string {
    // ✅ 最佳实践：预分配内存
    // 如果你知道大概有多长，使用 Grow() 可以避免多次内存重新分配
    // 这在高性能场景（如高频日志、序列化）非常关键
    var sb strings.Builder
    sb.Grow(1024) // 假设我们预估会有 1KB 左右的数据

    // 写入头部
    sb.WriteString("INSERT INTO users (name) VALUES ")

    for i, user := range users {
        if i > 0 {
            sb.WriteString(", ")
        }
        // 写入数据部分
        sb.WriteString("('")
        sb.WriteString(user)
        sb.WriteString("')")
    }

    sb.WriteString(";")

    // String() 方法会把 Builder 里的字节数组转换成字符串返回
    // 这一步非常高效，几乎没有内存拷贝
    return sb.String()
}

func main() {
    data := []string{"Alice", "Bob", "Charlie", "David"}
    query := GenerateSQL(data)
    fmt.Println(query)
}