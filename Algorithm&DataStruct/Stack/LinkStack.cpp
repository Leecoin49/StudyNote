#include<iostream>
#include <bits/stdc++.h>
using namespace std;

typedef int ElemType;
#define MaxSize 50

// 定义节点
typedef struct LinkNode{
    ElemType data;
    struct LinkNode *next;
}LinkNode, *LinkStack;

bool InitStack(LinkStack &L){
    L = (LinkNode *)malloc(sizeof(LinkNode));
    L -> next = NULL;
    L -> data = 0;
}

// 入栈
bool Push(LinkStack &L, ElemType e){
    if(L -> data == MaxSize-1){
        return false;
    }
    L -> data++;

    LinkNode *S = (LinkNode *)malloc(sizeof(LinkNode));
    S -> data = e;
    S -> next = L -> next;
    L -> next = S;

    return true;
}

// 出栈
bool Pop(LinkStack &L, ElemType &e){
    if(L->data == 0){
        return false;
    }
    e = L -> next -> data;
    L -> data--;

    LinkNode *S = L -> next;
    L -> next = L -> next -> next;

    free(S);

    return true;
}