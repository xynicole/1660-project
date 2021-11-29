FROM python:3
RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app


#ENV FLASK_APP=app.py

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000
CMD ["python", "app.py", "--host=0.0.0.0"]