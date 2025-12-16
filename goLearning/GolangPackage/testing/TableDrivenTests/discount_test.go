package store

import "testing"

func TestCalculatePrice(t *testing.T) {
	// 1. 定义测试用结构体
	tests := []struct {
		name  string
		level string
		price float64
		want  float64
	}{
		// 2.填充表格数据
		{"Normal User", "Normal", 100.0, 100.0},
		{"VIP Discount", "VIP", 100.0, 80.0},
		{"Admin Discount", "Admin", 100.0, 50.0},
		{"Zero Price", "VIP", 0.0, 0.0},           // 边界测试
		{"Unknown Level", "Hacker", 100.0, 100.0}, // 默认行为测试
	}

	// 3.遍历表格
	for _, tt := range tests {
		// 4.使用 t.Run 创建子测试
		t.Run(tt.name, func(t *testing.T) {
			// t.Parallel()

			got := CalculatePrice(tt.level, tt.price)

			// 5.验证结果
			if got != tt.want {
				t.Errorf("CalculatePrice(%s, %f) = %f; want %f",
					tt.level, tt.price, got, tt.want)
			}
		})
	}
}
