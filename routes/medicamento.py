from fastapi import APIRouter, HTTPException,Request,status
from models.medicamento import medicamento
from controllers.medicamento import(
    crear_medicamento
    ,get_all
    ,get_one
    ,delete_medicamento
    ,update_medicamento
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

@router.delete("/{id}", tags=["Medicamento"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_medicamento_content(id:int):
    status: str=await delete_medicamento(id)
    return status

@router.put("/{id}",tags=["Medicamento"])
async def update_medicamento_information(medicamento_data: medicamento , id: int):
    medicamento_data.id = id
    result =await update_medicamento(medicamento_data)
    return result