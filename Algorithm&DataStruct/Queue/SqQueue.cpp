#include<iostream>
#include<stdio.h>
using namespace std;

typedef int ElemType;
#define MaxSize 50

// 定义节点
typedef struct{
    ElemType data[MaxSize];
    int front;
    int rear;
}SqQueue;

// 初始化
bool InitQueue(SqQueue &Q){
    Q.front = 0;
    Q.rear = 0;
    return true;
}

// 判空
bool isEmpty(SqQueue &Q){
    if(Q.front == Q.rear){
        return true;
    }else{
        return false;
    }
}

// 求队列长度
int QueueLength(SqQueue Q){
    return (Q.rear - Q.front + MaxSize) % MaxSize;
}

// 入队
bool EnQueue(SqQueue &Q, ElemType e){
    if((Q.rear + 1) % MaxSize == Q.front){
        return false;
    }
    Q.data[Q.rear] = e;
    Q.rear = (Q.rear + 1) % MaxSize;
    return true;
}

// 出队
bool DeQueue(SqQueue &Q, ElemType &e){
    if(isEmpty(Q)){
        return false;   //队列空的判断
    }
    e = Q.data[Q.front]; //将队头元素赋值给e
    Q.front = (Q.front + 1) % MaxSize;    //front指针向后移一位置，若到最后则转到数组头部
}