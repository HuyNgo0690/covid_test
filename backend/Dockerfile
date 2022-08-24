FROM python:3.9.6-alpine3.14

WORKDIR /app
USER root
# Install python packages
RUN python -m pip install --upgrade pip
RUN chmod -R 777 /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
ENV PYTHONPATH "/app"
ENV FLASK_APP "main.py"

EXPOSE 3001
CMD ["python", "main.py"]