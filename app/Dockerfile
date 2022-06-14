FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


WORKDIR /code/
COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system --deploy

COPY . /code/
COPY entrypoint.sh ./
RUN ["chmod", "+x", "entrypoint.sh"]
ENTRYPOINT ["./entrypoint.sh"]
