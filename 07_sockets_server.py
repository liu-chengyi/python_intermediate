import socket

# AF_INET is internet socket (tells the socket that you want to use IPv4 addresses)
# AF_INET6 is for IPv6, and AF_UNIX is for Unix domain sockets
# SOCK_STREAM is TCP, SOCK_DGRAM is UDP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# the (ip, port #) we want the socket to run on (as host)
# 127.0.0.1 is ip for local device
s.bind(('127.0.0.1', 55556))
# listen to see if someone wants to build connection
s.listen()

while True:
    # accept() is the function we want to use when a client is trying to connect to the socket
    # here we accept all clients trying to connect to us
    client, address = s.accept()
    print("Connected to {}".format(address))
    client.send("You are connected!".encode())
    client.close()

