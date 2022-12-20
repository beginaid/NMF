FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN ls
RUN pwd
RUN mkdir results
COPY ./src ./
