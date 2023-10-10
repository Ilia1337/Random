import time
import socket

main_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_sock.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)


main_sock.bind(("localhost",10000))     
main_sock.setblocking(False)        
main_sock.listen(5)
print("Сокет создан")

list_us = []
while True:
    try:
        new_sock,addr = main_sock.accept()
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
    time.sleep(0.1)