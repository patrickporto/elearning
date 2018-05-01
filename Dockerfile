FROM python:3.6-alpine
RUN set -ex && \
    apk add --no-cache --update gcc make git python3-dev
ADD . /opt/app
WORKDIR /opt/app
RUN set -ex && \
    pip install pipenv && pipenv install --system --deploy
CMD ["python", "ava/manage.py", "runserver"]
