FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/main.py
COPY ./app /code/app
COPY ./sql_app /code/sql_app

CMD ["python3", "./main.py"]
