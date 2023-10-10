import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgresql:papazhiv@localhost/thisisbase')

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250),nullable=False)
    damage = Column(Integer,default=20)
    hp = Column(Integer,default=100)



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

s = Session()

hero = Users (id = 123)
s.merge(hero)
s.commit()



