#include <stdio.h>
#include <stdlib.h>
using namespace std;

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    //创建新结点用于存储操作后的链表
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy -> next = NULL;
    struct ListNode* current = dummy;

    //进行连接
    while (list1 != NULL && list2 != NULL){
        if (list1 -> val >= list2 -> val){
            current -> next = list2;
            list2 = list2 -> next;
        } else{
            current -> next = list1;
            list1 = list1 -> next;
        }
        current = current -> next;
    }
    if (list1 != NULL){
        current -> next = list1;
    } else{
        current -> next = list2;
    }
    return dummy -> next;
}


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (list1 == nullptr) {
        return list2;
    } else if (list2 == nullptr) {
        return list1;
    } else if (list1->val < list2->val) {
        list1->next = mergeTwoLists(list1->next, list2);
        return list1;
    } else {
        list2->next = mergeTwoLists(list1, list2->next);
        return list2;
    }
}