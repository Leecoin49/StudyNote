package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

const (
	numberGoroutines = 4  // 4 个工人
	taskLoad         = 10 // 10 个任务
)

var wg sync.WaitGroup

func main() {
	// 1. 创建一个有缓冲通道，容量为 10
	// 这意味着我们可以一次性把 10 个任务全扔进去，主线程不会被阻塞
	tasks := make(chan string, taskLoad)

	// 2. 启动 4 个 Goroutine (工人)
	wg.Add(numberGoroutines)
	for gr := 1; gr <= numberGoroutines; gr++ {
		go worker(tasks, gr)
	}

	// 3. 发布任务
	for post := 1; post <= taskLoad; post++ {
		tasks <- fmt.Sprintf("任务 %d", post)
	}

	// 4. 关闭通道
	// 关键点：关闭通道后，工人依然可以把通道里【剩余】的数据读完。
	// 读完后，他们会收到 close 信号从而退出。
	close(tasks)

	// 5. 等待所有工作完成
	wg.Wait()
}

func worker(tasks chan string, worker int) {
	defer wg.Done()

	for {
		// 消费者循环
		task, ok := <-tasks
		if !ok {
			// 通道已关闭且为空，工人下班
			fmt.Printf("工人 %d : 准备下班\n", worker)
			return
		}

		// 模拟工作
		fmt.Printf("工人 %d : 开始处理 %s\n", worker, task)
		sleep := rand.Int63n(100)
		time.Sleep(time.Duration(sleep) * time.Millisecond)
		fmt.Printf("工人 %d : 完成 %s\n", worker, task)
	}
}