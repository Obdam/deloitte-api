FROM python:3.9.0-alpine
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
CMD ["python", "app.py"]