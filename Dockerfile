FROM python:3.8-alpine

RUN apk update && apk add --no-cache gcc git python3-dev linux-headers musl-dev libffi-dev rust cargo openssl-dev

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD flask run --host=0.0.0.0 --port=5000