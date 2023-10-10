import time
import socket

main_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,1)



main_sock.bind(("localhost",10000))     
main_sock.setblocking(False)        
main_sock.listen(5)
print("Сокет создан")

while True:
    try:
        new_sock,addr = main_sock.accept()
        print("Подключился!",addr)
        new_sock.setblocking(False)                                ,
    except BlockingIOError:
        pass      