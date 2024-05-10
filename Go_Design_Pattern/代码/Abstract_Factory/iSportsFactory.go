/*
抽象工厂接口
*/
package main

import "fmt"

// 代码实现了一个ISportsFactory接口，该接口定义了makeShoe和makeShirt两个方法，用于创建运动鞋和运动衫。
type ISportsFactory interface {
	//makeShoe是一个方法名，IShoe是这个方法返回的类型。
	makeShoe() IShoe
	makeShirt() IShirt
}

func GetSportsFactory(brand string) (ISportsFactory, error) {
	if brand == "adidas" {
		/*
			在Go语言中，&Adidas{}是一个创建并返回新对象的表达式。
			这个表达式使用了结构体字面量（struct literal）和地址操作符&。

			Adidas是一个结构体类型的名字。
			{}是初始化这个结构体类型的字面量，它提供了结构体的实例化形式，但没有提供任何字段的初始值。

			在Go中，如果你不提供字段的初始值，那么结构体的字段会被自动初始化为其类型的零值。
			&是取地址操作符，它取得结构体字面量{}的内存地址，并返回一个指向该结构体的指针。

			因此，&Adidas{}创建了一个新的Adidas类型的实例，并返回了一个指向这个实例的指针。
			在上下文中，这个表达式是在工厂方法GetSportsFactory中，根据传入的品牌字符串brand来决定返回哪个品牌的工厂实例。

			如果brand是"adidas"，那么方法就会创建一个新的Adidas类型的实例，并返回它的指针（&Adidas{}），同时返回一个nil错误，表示操作成功且没有错误发生。
			这样，调用者就可以接收到一个指向Adidas工厂实例的指针，并使用这个指针来调用工厂方法创建adidas品牌的运动鞋和衬衫。
		*/
		return &Adidas{}, nil
	}

	if brand == "nike" {
		return &Nike{}, nil
	}

	return nil, fmt.Errorf("Wrong brand type passed")
}

//字面量（Literal）在编程语言中指的是一种表示固定值的表示法，它直接在源代码中表示了这个值。
//字面量可以表示各种基本数据类型的值，如整数、浮点数、布尔值、字符串等。
//在Go语言中，字面量用于创建和初始化变量，或者在表达式中直接表示一个值。
//例如，在Go语言中，以下是一些常见的字面量：
//整数字面量：42，-3，0x1A（十六进制表示的26）
//浮点数字面量：3.14，-0.001，0.1e-3（科学计数法表示的0.001）
//布尔字面量：true，false
//字符串字面量："Hello, world!"，'\n'（单个换行符）
