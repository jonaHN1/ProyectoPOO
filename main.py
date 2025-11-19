import uvicorn
from fastapi import FastAPI
from routes.medicamento import router as router_medicamento

app = FastAPI()

app.include_router(router_medicamento)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
