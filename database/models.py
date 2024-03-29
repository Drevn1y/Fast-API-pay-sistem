from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship

from database import Base


# Таблица пользователя
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    lastname = Column(String)
    phone_number = Column(Integer, unique=True)
    email = Column(String, unique=True)
    country = Column(String)
    reg_date = Column(DateTime)


# Таблица карт пользователя
class UserCard(Base):
    __tablename__ = 'cards'
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    card_name = Column(String)
    card_number = Column(Integer, nullable=False, unique=True)
    balance = Column(Float, default=0)
    exp_date = Column(Integer)

    user_fk = relationship(User, lazy='subquery')


# Таблица перевода - Транзакция
class Transfer(Base):
    __tablename__ = 'transfers'
    transfer_id = Column(Integer, primary_key=True, autoincrement=True)
    card_from_number = Column(Integer, ForeignKey('cards.card_number'))
    card_to_number = Column(Integer, ForeignKey('cards.card_number'))
    amount = Column(Float)

    status = Column(Boolean, default=True)
    transaction_date = Column(DateTime)

    card_from_fk = relationship(UserCard, lazy='subquery')
    card_to_fk = relationship(UserCard, lazy='subquery')

