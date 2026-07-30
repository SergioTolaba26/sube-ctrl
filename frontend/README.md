
cd frontend
python -m http.server 5500

http://localhost:5500

Ejecutar la API
cd backend
uvicorn main:app --reload

http://127.0.0.1:8000/ejercicios