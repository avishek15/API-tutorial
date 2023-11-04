FROM python:3.10.13-alpine3.17

WORKDIR /

COPY requirements.txt /

RUN pip3 install -r requirements.txt

COPY my_API.py /

CMD ["uvicorn", "my_API:app"]
