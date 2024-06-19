FROM python:3.12-slim
RUN apt-get update && apt-get install -y git build-essential
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/tatsy/torchmcubes.git
EXPOSE 5000
CMD python app.py