from typing import Optional
import faker
from sql_app.schemas import UserCreate
import requests

# Fake data
fake = faker.Faker()

# Request
URL = "http://localhost:8000"

for _ in range(100):
    fake_user = UserCreate(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.ascii_free_email(),
        address=fake.address(),
        phone_num=fake.phone_number(),
    )

    user_dict = fake_user.dict()
    req = requests.post(url=f"{URL}/users", json=user_dict)

    print(req.text)
