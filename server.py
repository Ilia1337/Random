# импорт модюля time и socket
import time
import socket
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import pygame

pygame.init()

WIDTH_ROOM,HEIGHT_ROOM = 4000,4000
WIDTH_SERVER,HEIGHT_SERVER = 300,300 
FPS = 60



# создание сокетов (AF_INET - используется семейства ipv4, SOCK_STREAM - используется протокол TCP, TCP_NODELAY - отключение задержки TCP)
main_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_sock.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)

# настройка сервера (local host - сервер на компе, 1000 - порт, SETBLOCKING - отключение выключения сервера при заканчиваннии обработки 1 клиента, listen - количество прослушиваемых клиентов.)
main_sock.bind(("localhost",10000))     
main_sock.setblocking(False)        
main_sock.listen(5)
print("Сокет создан")

# создание соеденения с pgadmin4 (в будущем engin)
engine = create_engine('postgresql+psycopg2://postgres:papazhiv@localhost/postgres')
Session = sessionmaker(bind=engine)
Base = declarative_base()
s = Session()

# создание окна (название,задание разрешения)
screen = pygame.display.set_mode((WIDTH_SERVER,HEIGHT_SERVER))
pygame.display.set_caption("СЕРВЕР")

# фпс
clock = pygame.time.Clock()

# создаём класс игрока и неаследуемся от базы 
class Player(Base):
    __tablename__ = 'gamers' 
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(250))
    adres = Column(String)
    x = Column(Integer, default=500)
    y = Column(Integer, default=500)
    size = Column(Integer, default=50)
    errors = Column(Integer,default= 0)
    abs_speed = Column(Integer, default=1)
    speed_x = Column(Integer, default=0)
    speed_y = Column(Integer, default=0)
    
    # иницилизируем класс
    def __init__(self,name,adres):
        self.name = name
        self.adres = adres
                                    
# создаём класс локального игрока
class Local_player:
    def __init__(self,id,name,sock,adres):
        self.id = id
        self.db: Player = s.get(Player,self.id)
        self.name = name
        self.sock = sock
        self.adres = adres
        self.x = 500
        self.y = 500
        self.size = 50 
        self.errors = 0
        self.abs_speed = 1 
        self.speed_x = 0
        self.speed_y = 0


Base.metadata.create_all(engine)

# цикл соединения с клиентом (recv - количество байт кодировки, decode - декодироват ь сообзение)
list_us = {}
while True:
    clock.tick(FPS)
    
    # принятие игрока
    try:
        new_sock,addr = main_sock.accept()                                         
        print("Подключился!",addr)
        new_sock.setblocking(False)                 
        
        # получаем адресс и сохжраняем данные о нём ы дб
        player = Player("Имя",addr)
        s.merge(player)
        s.commit()
    
        # фильтруем по адресу и ищем игрока
        addr = f'({addr[0]},{addr[1]})'
        data = s.query(Player).filter(Player.adres == addr)
        
        # проверяем айди
        for user in data:
            player = Local_player(user.id, "Имя", new_sock,addr)
            list_us[user.id] = player
        
        # получение данных
    except BlockingIOError:
        pass   
        
        for id in list(list_us):
            try:
                data = list_us[id].sock.recv(1024).decode()
                print("Получил", data)
            except:
                pass
        
        # проверяем не вышел ли игрок и закрываем сервер
        for id in list(list_us):
            try:
                list_us[id].sock.send("Игра".encode())
            except:
                list_us[id].sock.close()
                del list_us[id]            
                s.query(Player).filter(Player.id == id).delete()
                s.commit()
                print("Сокет закрыт")    