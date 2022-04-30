# base python image.
FROM python:3.8-slim-buster

# current working directory.
WORKDIR /

# copy the dependenices file for installation.
COPY requirements.txt requirements.txt

# install the python dependenices.
RUN pip3 install --no-cache-dir -r requirements.txt

# copy everything into directory.
COPY . .

# chnage the permission of the bash file.
RUN chmod +x ./app.sh

# trigger the bash file.
ENTRYPOINT ["sh", "./app.sh"]