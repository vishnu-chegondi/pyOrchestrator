FROM python:3.9

WORKDIR /app

RUN pip install pipenv

COPY Pipfile /app/

COPY Pipfile.lock /app/

RUN pipenv install

COPY . /app/

CMD pipenv run python3 main.py