FROM python:3.6-alpine
RUN set -ex && \
    apk add --no-cache --update build-base git python3-dev zlib-dev
ADD . /opt/app
WORKDIR /opt/app
RUN set -ex && \
    pip install pipenv && pipenv install --system --deploy
CMD ["python", "ava/manage.py", "runserver", "0.0.0.0:8000"]
