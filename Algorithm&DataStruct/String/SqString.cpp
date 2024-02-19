#include<iostream>
#include<stdio.h>
using namespace std;

#define MaxLen 255

//定义节点
typedef struct{
    char ch[MaxLen];
    int length;
}SqString;

// 求串长
int StrLength(SqString S){
    return S.length;
}

// 求字串
SqString SubString(SqString &Sub, SqString S, int pos, int len){
    Sub.ch[0] = S.ch[pos - 1];
    for(int i = 1; i <= len; i++){
        Sub.ch[i] = S.ch[pos - 1 + i];
    }

    return Sub;
}

int StrCompare(SqString S, SqString T) {
    int i=1;
    if(S.ch[0]==T.ch[0]) {
        while(i<=S.length) {
            if(S.ch[i]!=T.ch[i])
                return S.ch[i]-T.ch[i];
            i++;
        }
        if(i>S.length)
            return 0;
    }
    return S.ch[0]-T.ch[0];
}

// 定位函数
int Index(SqString S, SqString T){
    int i = 1, n = StrLength(S), m = StrLength(T);
    SqString sub;
    while(i <= n - m + 1){
        SubString(sub, S, i, m);
        if(StrCompare(sub, T) != 0){
            ++i;
        }else{
            return i;
        }
    }
    return 0;
}

int Index(SqString S, SqString T){
    int i = 1, j = 1;
    while(i <= S.length && j <= T.length){
        if(S.ch[i] == T.ch[j]){
            i++; j++;
        }else{
            i = i - j + 2;
            j = 1;
        }
    }
    if(j > T.length){
        return i - T.length;
    }else{
        return 0;
    }
}