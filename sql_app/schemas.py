from typing import Optional
from pydantic import BaseModel


class BankTransactionBase(BaseModel):
    amount: int
    sender_account_num: int
    receiver_account_num: int


class BankTransactionCreate(BankTransactionBase):
    pass


class BankTransaction(BankTransactionBase):
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    address: Optional[str]
    phone_num: Optional[str]


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    transactions: list[BankTransaction]

    class Config:
        orm_mode = True
