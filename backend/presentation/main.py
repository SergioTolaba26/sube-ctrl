from fastapi import FastAPI

app = FastAPI(
    title="Sistema Contable API",
    version="1.0.0",
)


@app.get("/")
def root():

    return {
        "mensaje": "Sistema Contable API funcionando",
    }