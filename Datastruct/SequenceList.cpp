#include <iostream>
#include <cstdio>
#include <stdlib.h>  // malloc��free ��ͷ�ļ� 
using namespace std;
 
 
#define InitSize 10  // Ĭ�ϵ���󳤶� 
 
 
typedef struct{
	int *data;  // ָʾ��̬���������ָ�� ��ָ���һ������Ԫ�� 
	int MaxSize;  // ˳������������ 
	int length;  // ˳���ĵ�ǰ���� 
}SeqList;  // ˳�������Ͷ��壨��̬���䷽ʽ�� 
 
 
void InitList(SeqList &L){
	// �� malloc ��������һƬ�����Ĵ洢�ռ�
	cout << "InitList(SeqList &L)��ʼ����..." << endl;
	L.data = (int *)malloc(InitSize * sizeof(int));
	L.length = 0;
	L.MaxSize = InitSize; 
	cout << "InitList(SeqList &L)��ʼ��������" << endl;
} 
 
 
// ���Ӷ�̬����ĳ���
void IncreaseSize(SeqList &L, int len){
	cout << "IncreaseSize(SeqList &L, int len)���Ӷ�̬���鳤����..." << endl;
	int *p = L.data;
	L.data = (int *)malloc((L.MaxSize + len) * sizeof(int));
	for(int i = 0; i < L.length; i++){
		L.data[i] = p[i];  // �����ݸ��Ƶ������� 
	}
	L.MaxSize = L.MaxSize + len;  // ˳�����󳤶����� 
	free(p);  // �ͷ�ԭ�����ڴ�ռ� 
	cout << "IncreaseSize(SeqList &L, int len)���Ӷ�̬���������" << endl;
} 
 
 
int main(){
	SeqList L;  // ����һ��˳���
	InitList(L);  // ��ʼ��˳���
	// ...��˳����������뼸��Ԫ��
	// ��ʱ lenth �� MaxSize ��ֵ��Ϊ 10 
	IncreaseSize(L, 5); 
	
	return 0
