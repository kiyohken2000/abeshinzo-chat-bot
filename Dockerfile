FROM python:3.9

ENV APP_HOME /hello-api
WORKDIR $APP_HOME
COPY . .

RUN pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 4 --threads 8 hello-api:app