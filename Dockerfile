FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /shopperz-api
WORKDIR /shopperz-api
COPY requirements.txt /shopperz-api/
RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps
COPY ./shopperz /shopperz-api/

RUN adduser -D thywoe
USER thywoe

# ENV DEBUG True
# RUN python manage.py makemigrations