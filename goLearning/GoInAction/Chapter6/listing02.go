// package main

// import (
// 	"fmt"
// 	"runtime"
// 	"sync"
// )

// var (
// 	// 【共享资源】
// 	counter int
// 	wg      sync.WaitGroup
// )

// func main() {
// 	wg.Add(2)

// 	// 启动两个 Goroutine，它们都试图修改 counter
// 	go incCounter(1)
// 	go incCounter(2)

// 	wg.Wait()
// 	fmt.Println("Final Counter:", counter)
// }

// func incCounter(id int) {
// 	defer wg.Done()

// 	for count := 0; count < 2; count++ {
// 		// --- 【临界区 Start】 ---
		
// 		// 1. Read: 捕获当前值
// 		value := counter 
		
// 		// 2. Context Switch: 
// 		// 这里调用 Gosched() 是为了【人为地】强制调度器暂停当前 Goroutine，
// 		// 让另一个 Goroutine 有机会插队运行。
// 		// 这模拟了现实中可能发生的不可预测的上下文切换。
// 		runtime.Gosched() 

// 		// 3. Modify: 本地增加
// 		value++

// 		// 4. Write: 写回共享变量
// 		// 如果在第 1 步和第 4 步之间，另一个 Goroutine 修改了 counter，
// 		// 这里的写回操作就会覆盖掉对方的修改！
// 		counter = value

// 		// --- 【临界区 End】 ---
// 	}
// }