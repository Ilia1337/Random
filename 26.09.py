from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.orm import declarative_base 
from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgresql:papazhiv@localhost/thisisbase")
zase = declarative_base()





class Users(zase):
    __tablename__= "Users"
    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String(250),nullable=False)
    damage = Column(Integer,default=20)
    hp = Column(Integer,default=100)

zase.metadata.create_all(engine)                                         
Sesion = sessionmaker(bind=engine)
s = Sesion()

u = Users(id = 1, name = "zlodei")
s.add(u)
s.commit()


