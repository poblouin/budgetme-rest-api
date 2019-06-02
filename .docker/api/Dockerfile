FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /budgetme
WORKDIR /budgetme
ADD requirements.txt /budgetme/
RUN pip install -r requirements.txt
ADD . /budgetme
