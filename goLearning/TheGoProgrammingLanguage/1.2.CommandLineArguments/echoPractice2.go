// package main

// import (
// 	"fmt"
// 	"os"
// 	"strings"
// )

// func main() {
// 	// print all index and value
// 	var s, sep string

// 	for i, arg := range os.Args[0:] {
// 		fmt.Println(strings.Repeat("*", 50))
// 		fmt.Println(i)
// 		fmt.Println(arg)
// 		fmt.Println(strings.Repeat("*", 50))
// 		s += sep + arg
// 		sep = " "
// 	}
// 	fmt.Println(s)
// }