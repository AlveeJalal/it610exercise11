FROM python:latest
WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY connecttodb.py connecttodb.py
CMD ["python", "-u", "connecttodb.py"]
