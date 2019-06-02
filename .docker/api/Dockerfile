FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /budgetme
WORKDIR /budgetme
RUN pip install pipenv
ADD Pipfile Pipfile.lock /budgetme/
RUN pipenv install --system --deploy --dev
ADD . /budgetme
