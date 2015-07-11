FROM ubuntu

VOLUME /docker/volumes/static:/media/static
RUN apt-get install -y python-setuptools
RUN easy_install pip

ADD req.txt /src/req.txt
RUN pip install -r /src/req.txt

ADD . /src

EXPOSE 8000
CMD python /src/web_host.py