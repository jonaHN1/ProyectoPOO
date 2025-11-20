from fastapi import APIRouter, HTTPException,Request,status
from models.venta import venta
from controllers.venta import(
    crear_venta
)

router = APIRouter(prefix="/Venta")

@router.post("/",tags=["Venta"])
async def crear_nueva_venta(venta_data: venta):
    result = await crear_venta(venta_data)

    return result

