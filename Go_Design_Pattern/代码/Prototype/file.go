// 具体原型
package main

import "fmt"

// //实现了Inode接口的类，它们负责创建自己的副本。
type File struct {
	name string
}

func (f *File) print(indentation string) {
	fmt.Println(indentation + f.name)
}

func (f *File) clone() Inode {
	return &File{name: f.name + "_clone"}
}
