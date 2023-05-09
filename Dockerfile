FROM ubuntu:latest
COPY [".", "/app"]
WORKDIR /app
RUN apt update -y && apt install python3 python3-pip -y
RUN pip3 install flask
EXPOSE 5000
CMD ["python3", "app.py"]

