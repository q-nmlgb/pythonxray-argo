FROM docker.io/meteor/galaxy-python:3.13.0
WORKDIR /app
COPY . .

RUN apt-get update && \
    apt-get install -y --no-install-recommends openssl bash curl ca-certificates && \
    rm -rf /var/lib/apt/lists/* && \
    chmod +x app.py && \
    pip install -r requirements.txt

CMD ["python", "app.py"]
