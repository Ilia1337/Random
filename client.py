# импорты
import socket
import time
import pygame
import math

# константы (WIDTH - высота, HEIGHT - ширина, CS - Центр экрана)
WIDTH = 800 
HEIGHT = 600
CS = (WIDTH//2,HEIGHT//2)

# помощь коду 
old_vector = (0,0)
radius = 50 

# сокеты (AF_INET - используется семейства ipv4, SOCK_STREAM - используется протокол TCP, TCP_NODELAY - отключение задержки TCP, 10000 - порт)
m2_sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
m2_sock.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
m2_sock.connect(("localhost",10000)) 

# иницилизация pygame и экрана (setmode - задание разрешения, setcaption - названия окна)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Бактерия")

# цикл закрытия (используется через run), вектора (getfocused, lenght - длинна)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # создание вектора 
        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            vector = pos[0]-CS[1],pos[1]-CS[1]
            length =  math.sqrt(vector[0]**2+vector[1]**2)
            vector = vector[0]/length, vector[1]/length                         

            # радиуса
            print(vector)         
            if length <= radius:
                vector = 0,0

            # сравнение с old.vector(0, 0)
            if vector != old_vector:
                old_vector = vector
                msg = f'<{vector[0]},{vector[1]}>'
                m2_sock.send(msg.encode())


                            
# отправка сообщение на сервер (recv - количество байт кодировки, decode - декодировать сообзение)
    # m2_sock.send("Кто жил и мыслил, тот не может в душе не презирать людей".encode())
    print("Файл отослан")
    data = m2_sock.recv(1024).decode()    
    print(f"Получено {data}") 
    
    
    # заливка фона окна и радиус круга 
    screen.fill("gray")
    pygame.draw.circle(screen,(255,0,0),CS,radius)
    pygame.display.update()
    # if vector:                                       

# выход из pygame
pygame.quit()
