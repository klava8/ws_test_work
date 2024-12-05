FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python ./manage.py makemigrations

RUN python ./manage.py migrate

CMD [ "python", "./manage.py", "runserver" ]