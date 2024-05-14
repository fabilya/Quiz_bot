FROM python:3

WORKDIR /app

COPY . .

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y ffmpeg
RUN pip install -r requirements.txt --no-cache-dir

