cd frontend en nootbook
python -m http.server 5500
http://localhost:5500

Ejecutar la API
cd backend en nootbook
uvicorn main:app --reload
http://127.0.0.1:8000/ejercicios

Cloud Conta en el celu con Server desde /frontend
c

API en el celu desde /backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

REFACTORIZACION -ELIMINAR ARQUITECTURA VIEJA
grep -R "/movimientos" -n frontend
0 (ningun archivo .py)
desde backend
grep -R "movimiento_router" -n .
0 (ningun archivo .py)
-------------------------------------------------
pytest tests/producto -v
------------------------------------------
pytest -q   pytest -x

source .venv/Scripts/activate

pytest tests/application/usecdcd_cases/movimiento/ -v


https://cloud-conta-backend.onrender.com/    idem/test-db

https://localhost:8000/empresas/        localhost:8000/test-db

https://cloud-conta-frontend.onrender.com/

Vemos si PostgreSQL está ok con este comando
stolaba@INN-NB005 MINGW64 /c/sube-ctrl/backend (main)
$ python -c "from dotenv import load_dotenv; load_dotenv(); from infrastructure.postgres.database import DatabasePostgres; db=DatabasePostgres(); print('POSTGRES OK')"