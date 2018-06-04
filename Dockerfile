FROM python:3.6-alpine
RUN set -ex && \
    apk add --no-cache --update build-base git python3-dev zlib-dev jpeg-dev nodejs
ADD . /opt/app
WORKDIR /opt/app
RUN set -ex && \
    pip install pipenv && pipenv install --system --deploy
RUN set -ex && \
    npm install
CMD ["python", "ava/manage.py", "runserver", "0.0.0.0:8000"]
