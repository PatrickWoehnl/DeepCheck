FROM python:3.7-slim-stretch
RUN apt-get update
RUN apt-get install g++ gcc libxslt-dev -y
RUN apt-get install libjpeg-dev libz-dev -y
RUN apt-get install gfortran libblas3 liblapack3 liblapack-dev libblas-dev -y
#RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
COPY ./requirements.txt /var/www/requirements.txt
WORKDIR /var/www/
RUN pip install --upgrade pip
RUN pip install -r /var/www/requirements.txt

expose 5000

CMD [ "python3", "/var/www/app/app.py"]