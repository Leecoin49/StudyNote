package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// 外层map：行文本 -> 内层map
	// 内层map：文件名 -> 该行在该文件中出现的次数
	counts := make(map[string]map[string]int)
	files := os.Args[1:]
	
	if len(files) == 0 {
		// 从标准输入读取，使用"stdin"作为文件名
		countLines(os.Stdin, "stdin", counts)
	} else {
		for _, filename := range files {
			f, err := os.Open(filename)
			if err != nil {
				fmt.Fprintf(os.Stderr, "dup2: %v\n", err)
				continue
			}
			countLines(f, filename, counts)
			f.Close()
		}
	}
	
	for line, fileMap := range counts {
		total := 0
		// 计算该行的总出现次数
		for _, count := range fileMap {
			total += count
		}
		
		// 只打印重复行
		if total > 1 {
			fmt.Printf("%d\t%s\n", total, line)
			// 打印出现该行的所有文件名
			for filename, count := range fileMap {
				if count > 0 {
					fmt.Printf("\t%s (%d次)\n", filename, count)
				}
			}
		}
	}
}

func countLines(f *os.File, filename string, counts map[string]map[string]int) {
	input := bufio.NewScanner(f)
	for input.Scan() {
		line := input.Text()
		// 如果该行还没有对应的内层map，创建一个
		if counts[line] == nil {
			counts[line] = make(map[string]int)
		}
		// 增加该行在该文件中的计数
		counts[line][filename]++
	}
}