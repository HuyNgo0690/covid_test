FROM python:3.10.6-alpine3.16

WORKDIR /app
USER root
# Add extra packages to install python cryptography
RUN apk add gcc musl-dev libffi-dev openssl-dev
# Install python packages
RUN pip install gunicorn
RUN chmod -R 777 /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app


EXPOSE 5000 5556
CMD ["python", "app.py"]