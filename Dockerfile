FROM python:3.8.7-slim-buster

WORKDIR /code
COPY requirements.txt /etc/

RUN apt-get clean && apt-get update && apt-get install -y make && \
    pip install -r /etc/requirements.txt \
                --no-cache-dir

COPY . .
CMD ["python", "main.py"]