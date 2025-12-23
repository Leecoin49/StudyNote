package main

import (
	"fmt"
	"sync"
)

var (
	counter int
	wg      sync.WaitGroup
	// 定义一把锁
	mutex sync.Mutex 
)

func main() {
	wg.Add(2)
	go incCounter(1)
	go incCounter(2)
	wg.Wait()
	fmt.Println("Final Counter:", counter)
}

func incCounter(id int) {
	defer wg.Done()
	for count := 0; count < 2; count++ {
		// 【临界区开始】
		// 进门先上锁。如果锁已经被别人拿了，我就在这里死等。
		mutex.Lock() 
		
		{ // 花括号不是必须的，但推荐加上，用于视觉上标记临界区
			value := counter
			// 即使这里发生 Context Switch，别人也进不来，
			// 因为他们会被卡在 mutex.Lock() 那里。
			value++ 
			counter = value
		}

		// 【临界区结束】
		// 出门开锁。必须执行，否则程序就死锁了（后面的人永远进不来）。
		mutex.Unlock() 
	}
}