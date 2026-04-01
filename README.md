# Servicio-de-APIREST-que-realice-las-operaciones-b-sicas-de-matem-ticas
API REST desarrollada con FastAPI para realizar operaciones matemáticas básicas (suma, resta, multiplicación y división) mediante solicitudes HTTP con JSON.

La API recibe datos en formato JSON y devuelve los resultados en formato JSON.


 Tecnologías utilizadas
- Python 3
- FastAPI
- Uvicorn

---

--- Instalación---

1. Clonar el repositorio:
bash
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO


2. Crear entorno virtual:
bash
python3 -m venv venv
source venv/bin/activate


3. Instalar dependencias:
bash
pip install -r requirements.txt


---

️ Ejecución

bash
uvicorn practica_1:app --reload

Luego abrir en el navegador:

http://127.0.0.1:8000/docs


---

--- Endpoints---

Suma
POST /suma

--

Ejemplo:

Entrada:
json
{
  "a": 5,
  "b": 3
}


Salida:
json
{
  "resultado": 8
}


---

Resta
POST /resta

Entrada:
json
{
  "a": 5,
  "b": 3
}


Salida:
json
{
  "resultado": 2
}


---

Multiplicación
POST /multiplicacion

Entrada:
json
{
  "a": 5,
  "b": 3
}


Salida:
json
{
  "resultado": 15
}

---

División
POST /division

Entrada:
json
{
  "a": 6,
  "b": 3
}


Salida:
json
{
  "resultado": 2
}


Error:
json
{
  "error": "No se puede dividir entre 0"
}

---

Todas las operaciones
POST /todo


Devuelve:
- suma
- resta
- multiplicación
- división

Entrada:
json
{
  "a": 10,
  "b": 2
}


Salida:
json
{
  "suma": 12,
  "resta": 8,
  "multiplicacion": 20,
  "division": 5
}

---

 Manejo de errores
- División entre 0 → retorna mensaje de error

---

Proyecto desarrollado por:
Jesús Eduardo Leal Gámez
