#include<iostream>
#include<stdio.h>
using namespace std;

typedef int ElemType;

void QuickSort(ElemType A[], int low, int high){
    ElemType pivot = Partition(A, low, high);
    QuickSort(A, low, pivot - 1);
    QuickSort(A, pivot + 1, high);
}

ElemType Partition(ElemType A[], int low, int high){
    int pivot = A[low];
    while(low < high){
        while(low < high && A[high] >= pivot){
            high--;
        }
        A[low] = A[high];
        while(low < high && A[low] <= pivot){
            low++;
        }
        A[high] = A[low];
    }
    A[low] = pivot;
    return low;
}