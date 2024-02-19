#include <windows.h>
#include <iostream>
#include <iomanip>		//setw（）函数所在库
#include<stdlib.h>
#include<time.h>
using namespace std;
 
void get_position()
{//获取鼠标位置坐标
    CONSOLE_CURSOR_INFO info = { 1, 0 };				//创建光标的属性结构体
    HANDLE hand = GetStdHandle(STD_OUTPUT_HANDLE);	//创建光标的句柄
    COORD coord = { 0, 0 };								//创建xy坐标结构体，用于设置光标位置
    POINT pt = { 0, 0 };								//创建鼠标点坐标变量
    SetConsoleCursorInfo(hand, &info);				//设置光标属性
    //循环显示
    int t = 100;//程序将在10s后退出
    while (1) {
        SetConsoleCursorPosition(hand, coord);		//传入光标句柄和坐标设置光标位置
        GetCursorPos(&pt);							//获取鼠标点的坐标位置
        cout << "当前坐标：" << pt.x << ',' << pt.y << setw(10) << "\0" << endl;	//输出坐标
 
        cout << "程序将在" << t / 10 << "s后继续 " << endl;;//在这段时间内可以获取想要点击的目标的坐标
        Sleep(100);
        if (t == 0) {break; }
        t = t - 1;
 
    }
    //循环显示结束
    
 
}
 
int mouseclick(int x,int y)
{
    // 模拟鼠标左键单击
    INPUT input;                //创建一个INPUT类型结构体
    input.type = INPUT_MOUSE;   //指定输入事件类型为鼠标事件
    input.mi.dwFlags = MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP; // 模拟鼠标左键按下和抬起的动作
    //mi是结构体INPUT的一个成员属性，mi是MOUSEINPUT类型
    //MOUSEINPUT 结构体用于描述鼠标事件，例如鼠标左键单击、双击、右键单击、移动等操作。
    SetCursorPos(x, y);
    input.mi.dx = 0;            //设置鼠标事件发生的x坐标
    input.mi.dy = 0;            //设置鼠标事件发生的y坐标
    input.mi.mouseData = 0;     //设置鼠标滚轮的滚动距离
    input.mi.dwExtraInfo = 0;   //将 dwExtraInfo 字段设置为 0，表示不传递任何附加的输入数据。
    input.mi.time = 0;          //time字段是用来设置时间戳的，0表示使用系统的时间戳
    SendInput(1, &input, sizeof(INPUT));
    /*SendInput函数是 Win32 API 中用于模拟输入事件的函数，可以模拟鼠标事件、键盘事件、硬件事件
    等。
    其函数原型如下：
        UINT SendInput(UINT nInputs, LPINPUT pInputs, int cbSize);
    其中，nInputs 参数指定输入事件的数量，pInputs 参数指向输入事件数组的指针，cbSize 参数指定输
    入事件数组的大小（单位为字节）。*/
    return 0;
}
 
 
 
int main()
{
    //首先获取到需要点击的位置坐标序列，这个函数调试时使用，获取到坐标简后可以注释掉
    get_position();
 
    // 将鼠标移动到特定的位置并单击，打开之前最小化到任务栏的程序
    mouseclick(400, 1068);
 
    //让程序睡眠1s再运行
    cout << "sleep 0.01s" << endl;
    Sleep(10);
 
    // 将鼠标移动到特定的位置并单击，在特定程序中执行点击操作
    mouseclick(1055, 578);
 
 
 
    return 0;
}
