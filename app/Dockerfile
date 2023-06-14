FROM python:3.11-slim

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

RUN python3 -m pip install --no-cache-dir flet==0.7.4

EXPOSE $PORT

CMD flet run --web --port $PORT main.py
