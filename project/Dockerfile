# Pull official base imagr
FROM python:3.9.2-slim-buster

# Set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependecies
RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

# Install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Add app
COPY . .