FROM python:3-alpine3.15

WORKDIR /personalsite

COPY . /personalsite

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python ./run.py