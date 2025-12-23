package main

import (
	"fmt"
	"sync"
	"sync/atomic" // 引入原子包
)

var (
	// 注意：原子操作通常要求特定类型的整数，如 int64
	counter int64
	wg      sync.WaitGroup
)

func main() {
	wg.Add(2)
	go incCounter(1)
	go incCounter(2)
	wg.Wait()
	fmt.Println("Final Counter:", counter) // 结果一定是 4
}

func incCounter(id int) {
	defer wg.Done()
	for count := 0; count < 2; count++ {
		// 【修复核心】：使用 atomic.AddInt64
		// 这一行代码在 CPU 看来是不可分割的指令。
		// 不会有任何 Goroutine 能在中间插队。
		atomic.AddInt64(&counter, 1)
	}
}