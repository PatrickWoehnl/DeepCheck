FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN apk add  jpeg-dev zlib-dev
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
WORKDIR /var/www/
RUN pip install --upgrade pip
RUN pip install -r /var/www/requirements.txt

expose 5000

CMD [ "python3", "/var/www/app/app.py"]