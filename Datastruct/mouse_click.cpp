#include <windows.h>
#include <iostream>
#include <iomanip>		//setw�����������ڿ�
#include<stdlib.h>
#include<time.h>
using namespace std;
 
void get_position()
{//��ȡ���λ������
    CONSOLE_CURSOR_INFO info = { 1, 0 };				//�����������Խṹ��
    HANDLE hand = GetStdHandle(STD_OUTPUT_HANDLE);	//�������ľ��
    COORD coord = { 0, 0 };								//����xy����ṹ�壬�������ù��λ��
    POINT pt = { 0, 0 };								//���������������
    SetConsoleCursorInfo(hand, &info);				//���ù������
    //ѭ����ʾ
    int t = 100;//������10s���˳�
    while (1) {
        SetConsoleCursorPosition(hand, coord);		//�����������������ù��λ��
        GetCursorPos(&pt);							//��ȡ���������λ��
        cout << "��ǰ���꣺" << pt.x << ',' << pt.y << setw(10) << "\0" << endl;	//�������
 
        cout << "������" << t / 10 << "s����� " << endl;;//�����ʱ���ڿ��Ի�ȡ��Ҫ�����Ŀ�������
        Sleep(100);
        if (t == 0) {break; }
        t = t - 1;
 
    }
    //ѭ����ʾ����
    
 
}
 
int mouseclick(int x,int y)
{
    // ģ������������
    INPUT input;                //����һ��INPUT���ͽṹ��
    input.type = INPUT_MOUSE;   //ָ�������¼�����Ϊ����¼�
    input.mi.dwFlags = MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP; // ģ�����������º�̧��Ķ���
    //mi�ǽṹ��INPUT��һ����Ա���ԣ�mi��MOUSEINPUT����
    //MOUSEINPUT �ṹ��������������¼�������������������˫�����Ҽ��������ƶ��Ȳ�����
    SetCursorPos(x, y);
    input.mi.dx = 0;            //��������¼�������x����
    input.mi.dy = 0;            //��������¼�������y����
    input.mi.mouseData = 0;     //���������ֵĹ�������
    input.mi.dwExtraInfo = 0;   //�� dwExtraInfo �ֶ�����Ϊ 0����ʾ�������κθ��ӵ��������ݡ�
    input.mi.time = 0;          //time�ֶ�����������ʱ����ģ�0��ʾʹ��ϵͳ��ʱ���
    SendInput(1, &input, sizeof(INPUT));
    /*SendInput������ Win32 API ������ģ�������¼��ĺ���������ģ������¼��������¼���Ӳ���¼�
    �ȡ�
    �亯��ԭ�����£�
        UINT SendInput(UINT nInputs, LPINPUT pInputs, int cbSize);
    ���У�nInputs ����ָ�������¼���������pInputs ����ָ�������¼������ָ�룬cbSize ����ָ����
    ���¼�����Ĵ�С����λΪ�ֽڣ���*/
    return 0;
}
 
 
 
int main()
{
    //���Ȼ�ȡ����Ҫ�����λ���������У������������ʱʹ�ã���ȡ�����������ע�͵�
    get_position();
 
    // ������ƶ����ض���λ�ò���������֮ǰ��С�����������ĳ���
    mouseclick(400, 1068);
 
    //�ó���˯��1s������
    cout << "sleep 0.01s" << endl;
    Sleep(10);
 
    // ������ƶ����ض���λ�ò����������ض�������ִ�е������
    mouseclick(1055, 578);
 
 
 
    return 0;
}
