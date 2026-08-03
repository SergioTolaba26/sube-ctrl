cd frontend en nootbook
python -m http.server 5500
http://localhost:5500

Ejecutar la API
cd backend en nootbook
uvicorn main:app --reload
http://127.0.0.1:8000/ejercicios

Cloud Conta en el celu con Server desde /frontend
http-server . -p 5500 -a 0.0.0.0
API en el celu desde /backend
uvicorn main:app
 --host 0.0.0.0 --port 8000 --reload
