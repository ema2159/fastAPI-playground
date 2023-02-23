from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True)
    address = Column(String)
    phone_num = Column(String)

    transactions_sent = relationship("BankTransaction", foreign_keys="BankTransaction.sender_id")
    transactions_received = relationship("BankTransaction", foreign_keys="BankTransaction.receiver_id")

class BankTransaction(Base):
    __tablename__ = "bank_transaction"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    timestamp = Column(DateTime)
    sender_id = Column(Integer, ForeignKey("user.id"))
    receiver_id = Column(Integer, ForeignKey("user.id"))

    sender = relationship("User", foreign_keys=[sender_id], overlaps="transactions_sent")
    receiver = relationship("User", foreign_keys=[receiver_id], overlaps="transactions_received")
