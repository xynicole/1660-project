FROM python:3
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN python3 driver.py
CMD ["python3", "driver.py"]


