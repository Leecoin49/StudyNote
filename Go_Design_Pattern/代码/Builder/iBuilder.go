// 生成器接口

package main

/*
定义了建造过程中需要执行的步骤。
在这个例子中，包括设置窗户类型（setWindowType）、设置门类型（setDoorType）和设置楼层数（setNumFloor）。
*/
type IBuilder interface {
	setWindowType()
	setDoorType()
	setNumFloor()
	getHouse() House
}

func getBuilder(builderType string) IBuilder {
	if builderType == "normal" {
		return newNormalBuilder()
	}

	if builderType == "igloo" {
		return newIglooBuilder()
	}
	return nil
}
