FROM python:3.10-alpine

RUN apk add --update curl bash \
    && pip install --upgrade pip \
    && pip install django pyquery requests \
    && rm -rf /var/cache/apk/* \

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN touch ./cronjob.tmp
RUN ./crontab.sh > ./cronjob.tmp
RUN chmod 644 ./cronjob.tmp
RUN crontab ./cronjob.tmp
RUN touch /var/log/cron.log
RUN rm -f ./crontab.sh && \
    rm -f ./cronjob.tmp && \
    rm -f ./.dockerignore

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]