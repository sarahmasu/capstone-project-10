FROM python:latest

WORKDIR /capstone-project-10

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /capstone-project-10

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]