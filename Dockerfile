FROM python:3.8-slim-buster

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x ./app.sh

ENTRYPOINT ["sh", "./app.sh"]