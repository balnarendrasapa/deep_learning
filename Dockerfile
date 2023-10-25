FROM ubuntu:latest

# Install make command, pip, python3, and python3-venv
RUN apt-get update && apt-get install -y make python3 python3-pip python3-venv

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["make", "run"]