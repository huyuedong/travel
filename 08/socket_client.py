#!/usr/bin/env python
#-*-coding:utf-8-*-
# client
import socket
client = socket.socket()

client.connect(('localhost',9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024)
    print("命令结果大小：",cmd_res_size)
    client.send("准备好啦！".encode("utf-8"))    # 防止粘包
    received_size = 0
    received_data = b''
    while received_size != int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data)
        received_data += data
    else:
        print("cmd res receive done...",received_size)
        print(received_data.decode())
client.close()