FROM python:latest
WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY app/ .
CMD ["python", "-u", "connecttodb.py"]
