from fastapi import APIRouter, HTTPException,Request,status
from models.cliente import cliente
from controllers.cliente import(
    crear_cliente
    ,get_all
    ,get_one
    ,delete_cliente
    ,update_cliente
)

router = APIRouter(prefix="/Cliente")

@router.post("/",tags=["Cliente"])
async def crear_nuevo_cliente(cliente_data: cliente):
    result = await crear_cliente(cliente_data)

    return result

@router.get("/",tags=["Cliente"])
async def get_all_cliente():
    result = await get_all()
    return result

@router.get("/{id}",tags=["Cliente"])
async def get_one_cliente(id:int):
    result : cliente = await get_one(id)
    return result

@router.delete("/{id}", tags=["Cliente"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_cliente_content(id:int):
    status: str=await delete_cliente(id)
    return status

@router.put("/{id}",tags=["Cliente"])
async def update_cliente_information(cliente_data: cliente , id: int):
    cliente_data.id = id
    result =await update_cliente(cliente_data)
    return result