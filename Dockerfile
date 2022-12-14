FROM alpine:3.16.2
WORKDIR /app
COPY . /app
EXPOSE 5000
RUN apk add --update py-pip
RUN pip install -r requirements.txt
CMD python3 ./app.py