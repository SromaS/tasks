FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install pipenv
COPY Pipfile* /code/
RUN cd /code && pipenv lock --requirements > requirements.txt
RUN pipenv install --system

COPY . /code/
