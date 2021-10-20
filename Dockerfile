FROM python:3.9.6
WORKDIR /app
COPY  requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN pip install python-telegram-bot
CMD [ "python", "./main.py" ]
