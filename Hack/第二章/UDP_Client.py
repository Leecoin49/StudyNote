import socket

target_host = "10.17.213.74"
target_port = 9998

# create a socket object
# AF_INET: standard IPv4 address or hostname; SOCK_DGRAM: this is a UDP client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# connect the client to the server
# client.connect((target_host, target_port))

# send some data as bytes
client.sendto(b"AAABBBCCC",(target_host,target_port))

# receive some data back
data, addr = client.recvfrom(4096)

# printout the response
print(data.decode())
# close the socket client
client.close()
