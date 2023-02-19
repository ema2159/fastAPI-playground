from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True)
    address = Column(String)
    phone_num = Column(String)

    # transactions = relationship("Transaction", back_populates=True)


# class Transaction(Base):
#     __tablename__ = "transaction"

#     amount = Column(Integer)
#     id = Column(Integer, primary_key=True, index=True)
#     user1_id = Column(Integer, ForeignKey("user.id"))
#     user2_id = Column(Integer, ForeignKey("user.id"))

#     user = relationship("User", back_populates=True)
