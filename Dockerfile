FROM python:3.11-alpine

RUN apk update
RUN apk add git

WORKDIR /TemplateGenerator
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
COPY TemplateGenerator .

EXPOSE 5000

CMD [ "python3", "-m", "flask", "run"]
