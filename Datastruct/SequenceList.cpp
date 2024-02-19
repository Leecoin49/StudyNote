#include <iostream>
#include <cstdio>
#include <stdlib.h>  // malloc、free 的头文件 
using namespace std;
 
 
#define InitSize 10  // 默认的最大长度 
 
 
typedef struct{
	int *data;  // 指示动态分配数组的指针 ，指向第一个数据元素 
	int MaxSize;  // 顺序表的做大容量 
	int length;  // 顺序表的当前长度 
}SeqList;  // 顺序表的类型定义（动态分配方式） 
 
 
void InitList(SeqList &L){
	// 用 malloc 函数申请一片连续的存储空间
	cout << "InitList(SeqList &L)初始化中..." << endl;
	L.data = (int *)malloc(InitSize * sizeof(int));
	L.length = 0;
	L.MaxSize = InitSize; 
	cout << "InitList(SeqList &L)初始化结束！" << endl;
} 
 
 
// 增加动态数组的长度
void IncreaseSize(SeqList &L, int len){
	cout << "IncreaseSize(SeqList &L, int len)增加动态数组长度中..." << endl;
	int *p = L.data;
	L.data = (int *)malloc((L.MaxSize + len) * sizeof(int));
	for(int i = 0; i < L.length; i++){
		L.data[i] = p[i];  // 将数据复制到新区域 
	}
	L.MaxSize = L.MaxSize + len;  // 顺序表最大长度增加 
	free(p);  // 释放原来的内存空间 
	cout << "IncreaseSize(SeqList &L, int len)增加动态数组结束！" << endl;
} 
 
 
int main(){
	SeqList L;  // 声明一个顺序表
	InitList(L);  // 初始化顺序表
	// ...往顺序表中随便插入几个元素
	// 此时 lenth 与 MaxSize 的值都为 10 
	IncreaseSize(L, 5); 
	
	return 0
