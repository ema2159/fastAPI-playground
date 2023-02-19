from typing import Optional
from pydantic import BaseModel


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


class BankTransactionBase(BaseModel):
    amount: int


class BankTransactionCreate(BankTransactionBase):
    pass


class BankTransaction(BankTransactionBase):
    class Config:
        orm_mode = True
