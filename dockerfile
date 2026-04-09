FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn

EXPOSE 8000

CMD ["uvicorn", "practica_1:app", "--host", "0.0.0.0", "--port", "8000"] 

