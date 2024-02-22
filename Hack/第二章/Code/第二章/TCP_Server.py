import socket
import threading

IP = '10.17.213.74'
PORT = 9998


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 指定服务器应该监听那个IP地址和端口。
    server.bind((IP, PORT))
    # 服务器开始监听，并把最大连接数设为5。
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    # 进入主循环，等待外来连接。
    while True:
        # 当一个客户端建立连接时，将接收到的客户端socket对象保存到client变量中，将远程连接的详细信息保存到address变量中。
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        # 创建线程并传入handle_client函数和client变量。
        client_handler = threading.Thread(target=handle_client, args=(client,))
        # 启动线程来处理接收到的连接。
        client_handler.start()


def handle_client(client_socket):
    with client_socket as sock:
        # 调用recv()接受数据，并给客户端发送一段简单的回复。
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')


if __name__ == '__main__':
    main()