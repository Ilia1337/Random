# импорты
import socket
import time
import pygame

# высота окна pygame
WIDTH = 800 
HEIGHT = 600
CS = (WIDTH//2,HEIGHT//2)

old_vector = (0,0)
radius = 50 

# сокеты
m2_sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            vector = pos[0]-CS[1],pos[1]-CS[1]
            if vector != old_vector:
                old_vector = vector
                msg = f'<{vector[0]},{vector[1]}>'
                m2_sock.send(msg.encode())


                            
# отправка сообщение на сервер
    # m2_sock.send("Кто жил и мыслил, тот не может в душе не презирать людей".encode())
    print("Файл отослан")
    data = m2_sock.recv(1024).decode()    
    print(f"Получено {data}") 
    
    
    
    screen.fill("gray")
    pygame.draw.circle(screen,(255,0,0),CS,radius)
    pygame.display.update()
    #if vector                                        


# выход из pygame
pygame.quit()
