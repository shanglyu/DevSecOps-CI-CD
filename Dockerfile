FROM python:3.10-bullseye

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

RUN python3 usersdb.py

RUN mv flag.txt /flag$(tr -dc 'a-zA-Z0-9' < /dev/urandom | fold -w 10 | head -n 1).txt

CMD [ "python3", "app.py" ]