from typing import Optional
import faker
from pydantic import BaseModel
import requests

# Fake data
fake = faker.Faker()


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    address: Optional[str]
    phone_num: Optional[str]

# Request

URL = "http://localhost:8000"

for _ in range(100):
    fake_user = User(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.ascii_free_email(),
        address=fake.address(),
        phone_num=fake.phone_number(),
    )

    user_dict = fake_user.dict()
    req = requests.post(url=f"{URL}/user", json=user_dict)

    print(req.text)
