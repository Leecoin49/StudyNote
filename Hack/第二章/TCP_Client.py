import socket

target_host = '10.17.213.74'
target_port = 9998

# create a socket object
# 创建一个带有AF_INET和SOCK_STREAM参数的socket对象。
# AF_INET参数表示我们将使用标准的IPv4地址或主机名。
# SOCK_STREAM表示这是一个TCP客户端。
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# 将客户端连接到服务器。
client.connect((target_host, target_port))

# send some data
# 发送一些bytes类型的数据。
client.send(b"Hello World!")
client.send(b"Hello My Friend!")

# receive some data
# 接受返回的数据并打印。
response = client.recv(4096)

print(response.decode())
client.close()