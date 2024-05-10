// 原型接口
package main

// 定义了原型模式中对象必须实现的通用接口。
// 在这个例子中，包括打印（print）和克隆（clone）两个方法。
type Inode interface {
	print(string)
	clone() Inode
}
