import uvicorn
from fastapi import FastAPI
from routes.medicamento import router as router_medicamento
from routes.cliente import router as router_cliente
from routes.venta import router as router_venta

app = FastAPI()

app.include_router(router_medicamento)
app.include_router(router_cliente)
app.include_router(router_venta)

@app.get("/")
def read_root():
    return {"Hello": "Medicamentos"
            ,"version": "0.1.0"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
