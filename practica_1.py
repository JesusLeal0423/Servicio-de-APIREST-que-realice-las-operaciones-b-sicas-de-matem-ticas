from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numeros(BaseModel):
    a: float
    b: float

@app.get("/")
def root():
    return {"message": "API de operaciones"}

@app.post("/suma")
def suma(datos: Numeros):
    return {"resultado": datos.a + datos.b}

@app.post("/resta")
def resta(datos: Numeros):
    return {"resultado": datos.a - datos.b}

@app.post("/multiplicacion")
def multiplicacion(datos: Numeros):
    return {"resultado": datos.a * datos.b}

@app.post("/division")
def division(datos: Numeros):
    if datos.b == 0:
        return {"error": "No se puede dividir entre 0"}
    return {"resultado": datos.a / datos.b}

@app.post("/todo")
def todo(datos: Numeros):
    return {
        "suma": datos.a + datos.b,
        "resta": datos.a - datos.b,
        "multiplicacion": datos.a * datos.b,
        "division": "Error" if datos.b == 0 else datos.a / datos.b
    }