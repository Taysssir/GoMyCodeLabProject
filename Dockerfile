# pull the official base image
FROM python:3.8.3-alpine
RUN pip install --upgrade pip

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --no-cache jpeg-dev zlib-dev
    

COPY ./requirments.txt /usr/src/app
RUN pip install -r requirments.txt

# RUN pip install Pillow
USER root

# copy project
COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]