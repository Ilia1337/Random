import socket
import time
import pygame


m2_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
m2_sock.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
m2_sock.connect(("localhost",10000)) 


pygame.init()







while True:
    m2_sock.send("Кто жил и мыслил, тот не может в душе не презирать людей".encode())
    print("Файл отослан")
    time.sleep(0.5)