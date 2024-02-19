#include <iostream>
#include <bits/stdc++.h>
using namespace std;

# define MaxSize 50	//定义栈中元素的最大个数
typedef int ElemType;

typedef struct{
	ElemType data[MaxSize];
	int top;	//用于栈顶指针
}SqStack;

//初始化栈
void InitStack(SqStack &S){
	S.top = -1;
}

//判栈空
bool StackEmpty(SqStack S){
	if(S.top == -1){
		return true;
	}
	else{
		return false;
	}
}

//进栈
bool Push(SqStack &S, ElemType x){
	if(S.top == MaxSize-1){		//栈满，报错
		return false;
	}
	S.top++;
	S.data[S.top] = x;
	return true;
}

//出栈
bool Pop(SqStack &S, ElemType &x){
	if(S.top == -1){
		return false;
	}
	x = S.data[S.top];
	return true;
}

//读取栈顶元素
bool GetTop(SqStack &S, ElemType &x){
	if(S.top == -1){
		return false;
	}
	x = S.data[S.top];
	return true;
}

