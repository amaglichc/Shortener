FROM python:3.12

RUN apt-get update && apt-get install -y 

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8081