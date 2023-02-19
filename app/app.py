from fastapi import FastAPI
from sql_app.schemas import UserBase

app = FastAPI()



@app.get("/", tags=["ROOT"])
async def root():
    return {"Hello": "World"}


@app.post("/user", tags=["userAPI"])
async def post_user(user: UserBase):
    print(user)
    return "Success"
