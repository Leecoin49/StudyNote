package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup
var sum int

func add() {
	defer wg.Done() //函数执行完后,计数器减一
	for i := 0; i < 10000; i++ {
		sum++
	}
}
func main() {
	//设置计数为3代表要启动三个协程
	wg.Add(3)
	go add()
	go add()
	go add()
	wg.Wait()
	fmt.Println(sum)
}
