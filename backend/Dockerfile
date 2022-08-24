FROM python:3.8-alpine3.16

WORKDIR /app
USER root
# Install python packages
RUN python -m pip install --upgrade pip
RUN pip install gunicorn
RUN chmod -R 777 /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
ENV PYTHONPATH "/app"

EXPOSE 3001
CMD ["python", "app.py"]
#CMD ["sh", "start.sh"]