# импорты
import socket
import time
import pygame

# высота окна pygame
WIDTH = 800 
HEIGHT = 600

# сокеты 
m2_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
m2_sock.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
m2_sock.connect(("localhost",10000)) 

# инициирование pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Бактерия")

# цикл крестика
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# отправка сообщение на сервер
    m2_sock.send("Кто жил и мыслил, тот не может в душе не презирать людей".encode())
    print("Файл отослан")
    data = m2_sock.recv(1024).decode()    
    print(f"Получено {data}") 

# выход из pygame
pygame.quit()