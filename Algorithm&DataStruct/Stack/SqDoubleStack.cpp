#include <iostream>
#include <bits/stdc++.h>
using namespace std;

#define MaxSize 50
typedef int ElemType;

//定义共享栈
typedef struct{
    ElemType data[MaxSize];
    int top0;
    int top1;
}SqDoubleStack;

//进栈
bool Push(SqDoubleStack &S, ElemType x, int stackNumber){
    if(S.top0+1 == S.top1){
        return false;
    }
    if(stackNumber == 0){
        S.data[++S.top0] = x;
    }
    else if(stackNumber == 1){
        S.data[--S.top1] = x;
    }
    return true;
}

//出栈
bool Pop(SqDoubleStack &S, ElemType &x, int stackNumber){
    if(stackNumber == 0){
        if(S.top0 == -1){
            return false;
        }
        x = S.data[S.top0--];
    }
    else if(stackNumber == 1){
        if(S.top1 == MaxSize){
            return false;
        }
        x = S.data[S.top1++];
    }
    return true;
}