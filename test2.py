import socket

ip = '127.0.0.1'
port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('msg: ')
    sock.sendto(msg.encode(), (ip, port))
