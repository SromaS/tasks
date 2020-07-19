FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /code2/
RUN mkdir /data
RUN pip install pipenv
COPY Pipfile* /code2/
RUN cd /code2 && pipenv lock --requirements > requirements.txt
RUN pipenv install --system

COPY . /code2/
CMD ["sh", "migrations.sh"]