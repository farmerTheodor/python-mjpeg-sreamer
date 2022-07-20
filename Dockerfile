FROM python:3.8-slim

WORKDIR /usr/app


RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT python3 -u ./image_stream.py