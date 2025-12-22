// package main

// import (
// 	"fmt"
// 	"runtime"
// 	"sync"
// )

// // wg 用来等待程序完成，避免主程序在 Goroutine 还没跑完就退出了
// var wg sync.WaitGroup

// func main() {
// 	// 核心逻辑 1: 分配 1 个逻辑处理器给调度器使用
// 	// 这意味着，无论你电脑有几个核，Go 程序同一时间只能执行一个 Goroutine 的代码
// 	// 这里强制演示的是【并发】而非【并行】
// 	runtime.GOMAXPROCS(1)

// 	// 计数器加 2，表示我们要等待两个 Goroutine
// 	wg.Add(2)

// 	fmt.Println("开启 Goroutine")

// 	// 启动第一个 Goroutine：打印小写字母
// 	go printPrime("A")
// 	// 启动第二个 Goroutine：打印大写字母
// 	go printPrime("B")

// 	// 等待两个任务完成
// 	fmt.Println("等待执行结束...")
// 	wg.Wait()
// 	fmt.Println("\n程序结束")
// }

// // printPrime 显示字母（模拟耗时任务）
// func printPrime(prefix string) {
// 	// 通知 main 函数，这个 Goroutine 做完了
// 	defer wg.Done()

// next:
// 	for outer := 2; outer < 5000; outer++ {
// 		for inner := 2; inner < outer; inner++ {
// 			if outer%inner == 0 {
// 				continue next
// 			}
// 		}
// 		// 这里的计算是为了消耗 CPU 时间，触发调度器的切换
// 		fmt.Printf("%s:%d\n", prefix, outer)
// 	}
// 	fmt.Println("Completed", prefix)
// }