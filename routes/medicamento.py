from fastapi import APIRouter, HTTPException,Request
from models.medicamento import medicamento
from controllers.medicamento import(
    crear_medicamento
    ,get_all
    ,get_one
)

router = APIRouter(prefix="/medicamento")

@router.post("/",tags=["Medicamento"])
async def crear_nuevo_medicamento(medicamento_data: medicamento):
    result = await crear_medicamento(medicamento_data)

    return result

@router.get("/",tags=["Medicamento"])
async def get_all_medicamentos():
    result = await get_all()
    return result

@router.get("/{id}",tags=["Medicamento"])
async def get_one_medicamento(id:int):
    result : medicamento = await get_one(id)
    return result



