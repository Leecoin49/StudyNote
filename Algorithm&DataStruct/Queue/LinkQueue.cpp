#include<iostream>
#include<stdio.h>
using namespace std;

typedef int ElemType;
#define MaxSize 50

// 定义节点
typedef struct LinkNode{
    ElemType data;
    struct LinkNode *next;
}LinkNode;

// 定义链队列
typedef struct{
    LinkNode *front, *rear;
}*LinkQueue;

// 初始化
void InitQueue(LinkQueue &Q){
    Q -> front = Q -> rear = (LinkNode *)malloc(sizeof(LinkNode));
    Q -> front -> next = NULL;
}

// 入队
bool EnQueue(LinkQueue &L, ElemType e){
    LinkNode *s = (LinkNode *)malloc(sizeof(LinkNode));
    s -> data = e;
    s -> next = NULL;
    L -> rear -> next = s;
    L -> rear = s;
    return true;
}

// 出队
bool DeQueue(LinkQueue &L, ElemType &e){
    // 若队列为空则不出
    if(L -> front == L -> rear){
        return false;
    }
    LinkNode *p = (LinkNode *)malloc(sizeof(LinkNode));
    p = L -> front -> next;
    e = p -> data;
    L -> front -> next = p -> next;
    // 若删除的元素是队尾，则删除后队尾指向队首
    if(L -> rear == p){
        L -> rear = L -> front;
    }
    free(p);
    return true;
}