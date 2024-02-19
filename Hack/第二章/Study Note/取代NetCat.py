import argparse
import socket
import shlex
# 该库提供了一组强大的进程创建接口，让你可以通过多种方式调用其他程序。
import subprocess
import sys
import textwrap
import threading

# 这个函数将会接受一条命令并执行，然后将结果作为一段字符串返回。
def execute(cmd):
    cmd = cmd.strp()
    if not cmd:
        return
    # 我们用到了它的check_output函数，这个函数会在本机运行一条命令，并返回该命令的输出。
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()

# 用来解析命令行参数并调用其他函数。
if __name__ == "__main__":
    parser = argparse.ArgumentParser(   # 使用标准库里的argparse库创建了一个带命令行界面的程序❶，传递不同的参数，就能控制这个程序执行不同的操作，比如上传文件、远程执行命令，或是打开一个命令行shell。
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:  # 我们编写了一段帮助信息❷，程序启动的时候如果发现--help参数，
            netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell    
            netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt #upload to file
            netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" #execute command
            echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
            netcat.py -t 192.168.1.108 -p 5555 # connect to server
        ''')
    )
    parser.add_argument('-c', '--command', action='store_true', help='command shell')   # 就会显示这段信息。我们还添加了6个参数，用来控制程序的行为❸。
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
    parser.add_argument('-u', '--upload', help='upload file')
    args = parser.parse_args()
    if args.listen:
        # 程序收到-c参数，就会打开一个交互式的命令行shell；收到-e参数，就会执行一条命令；收到-l参数，就会创建一个监听器；-p参数用来指定要通信的端口；-t参数用来指定要通信的目标IP地址；
        # -u参数用来指定要上传的文件。因为发送方和接收方都会运行这个程序，所以传进来的参数会决定这个程序接下来是要发送数据还是要进行监听。使用了-c、-e和-u这三个参数，就意味着要使用-l参数，因为这些行为都只能由接收方来完成。
        # 而发送方只需要向接收方发起连接，所以它只需要用-t和-p两个参数来指定接收方。如果确定了程序要进行监听❹，我们就在缓冲区里填上空白数据，把空白缓冲区传给NetCat对象。反之，我们就把stdin里的数据通过缓冲区传进去。最后调用NetCat类的run函数来启动它。
        buffer = ''
    else:
        buffer = sys.stdin.read()

    nc = NetCat(args, buffer.encode())
    nc.run()
