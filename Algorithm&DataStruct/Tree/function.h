#include <stdio.h>
#include <stdlib.h>

typedef char BiElemType;
typedef struct BiTNode{
    BiElemType c;//c 就是书籍上的data
    struct BiTNode *lchild;
    struct BiTNode *rchild; 
}BiTNode,*BiTree;

//tag结构体是辅助队列使用的
typedef struct tag{
    BiTree p;//树的某一个结点的地址值
    struct tag *pnext;
}tag_t, *ptag_t;