package math

import (
    "testing"
)

// TestAdd 必须以 Test 开头，且接收一个 *testing.T 指针
func TestAdd(t *testing.T) {
    // 1. 准备输入
    a, b := 2, 2
    // 2. 期望结果
    expected := 3

    // 3. 执行目标函数
    actual := Add(a, b)

    // 4. 判断结果 (Go 没有 assert，直接用 if 判断)
    if actual != expected {
        // t.Errorf 是最常用的报错方式，格式化输出错误信息
        // 注意：这里不会中断测试，它只是标记为失败并继续运行
        t.Errorf("Add(%d, %d) = %d; want %d", a, b, actual, expected)
    }
}