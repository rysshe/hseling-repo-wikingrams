FROM python:3.7

RUN apt-get update \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8001
CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]