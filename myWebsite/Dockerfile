FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /myWebsite

ADD . /myWebsite/

EXPOSE 8000

COPY requirements.txt /myWebsite

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /myWebsite

ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver", "0.0.0.0:8000"]