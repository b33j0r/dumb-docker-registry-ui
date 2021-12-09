FROM python:3.9-alpine

RUN apk update && \
    apk upgrade && \
    apk add python3 py3-pip

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN python3 setup.py develop

EXPOSE 5858
CMD ["python3", "-m", "dumb.app"]
