from datetime import datetime
import json
import logging

from fastapi import HTTPException

from models.medicamento import medicamento
from utils.database import execute_query_json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



async def get_one( id: int ) -> medicamento:

    selectscript = """
        SELECT [id]
            ,[nombre]
            ,[fecha_vencimiento]
        FROM [FARMACIA].[MEDICAMENTO]
        WHERE id = ?
    """

    params = [id]
    result_dict =[]
    try:
        result = await execute_query_json(selectscript, params=params)
        result_dict = json.loads(result)

        if len(result_dict) > 0:
            return result_dict[0]
        else:
            raise HTTPException(status_code=404, detail=f"medicamento not found")

    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Database error: { str(e) }")


async def get_all() -> list[medicamento]:

    selectscript = """
        SELECT [id]
            ,[nombre]
            ,[fecha_vencimiento]
        FROM [FARMACIA].[MEDICAMENTO]
    """

    
    try:
        result = await execute_query_json(selectscript)
        result_dict = json.loads(result)
        return result_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")



async def crear_medicamento( medicamento: medicamento ) -> medicamento:

    sqlscript: str = """
        INSERT INTO [FARMACIA].[MEDICAMENTO] ([id], [nombre], [fecha_vencimiento])
        VALUES (?, ?, ?);
    """

    params = [
        medicamento.id,
        medicamento.nombre,
        medicamento.fecha_vencimiento

    ]

    insert_result = None
    try:
        insert_result = await execute_query_json( sqlscript, params, needs_commit=True )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")

    sqlfind: str = """
        SELECT [id]
            ,[nombre]
            ,[fecha_vencimiento]
        FROM [FARMACIA].[MEDICAMENTO]
        WHERE id = ? and nombre = ? and fecha_vencimiento = ?
    """
    
    params = [medicamento.id, medicamento.nombre ,medicamento.fecha_vencimiento]

    result_dict=[]
    try:
        result = await execute_query_json(sqlfind, params=params)
        result_dict = json.loads(result)

        if len(result_dict) > 0:
            return result_dict[0]
        else:
            return []
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")
