# импорты
import time
import socket

# создание сокетов
main_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_sock.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)

# слушание клиента
main_sock.bind(("localhost",10000))     
main_sock.setblocking(False)        
main_sock.listen(5)
print("Сокет создан")

# цикл соединения с клиентом
list_us = []
while True:
    try:
        new_sock,addr = main_sock.accept()
        print(list_us)
        print("Подключился!",addr)
        new_sock.setblocking(False)                 
        list_us.append(new_sock)
    except BlockingIOError:
        pass      
    for i in list_us:
            try:
                data = i.recv(1024).decode()
                print(f"Я получил {data}!")
                
            except:
                pass
    for sock in list_us:
        try:
            sock.send("Игра".encode())
        except:
            list_us.remove(sock)
            sock.close()
            print("Сокет закрыт")
    time.sleep(0.1)
    