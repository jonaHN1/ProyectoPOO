from datetime import datetime
import json
import logging

from fastapi import HTTPException

from models.cliente import cliente
from utils.database import execute_query_json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



async def get_one( id: int ) -> cliente:

    selectscript = """
        SELECT [id]
            ,[nombre]
            ,[fecha_nacimiento]
        FROM [FARMACIA].[CLIENTE]
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
            raise HTTPException(status_code=404, detail=f"cliente not found")

    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Database error: { str(e) }")


async def get_all() -> list[cliente]:

    selectscript = """
        SELECT [id]
            ,[nombre]
            ,[fecha_nacimiento]
        FROM [FARMACIA].[CLIENTE]
    """

    
    try:
        result = await execute_query_json(selectscript)
        result_dict = json.loads(result)
        return result_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")



async def crear_cliente( cliente: cliente ) -> cliente:

    sqlscript: str = """
        INSERT INTO [FARMACIA].[CLIENTE] ([id], [nombre], [fecha_nacimiento])
        VALUES (?, ?, ?);
    """

    params = [
        cliente.id,
        cliente.nombre,
        cliente.fecha_nacimiento

    ]

    insert_result = None
    try:
        insert_result = await execute_query_json( sqlscript, params, needs_commit=True )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")

    sqlfind: str = """
        SELECT [id]
            ,[nombre]
            ,[fecha_nacimiento]
        FROM [FARMACIA].[CLIENTE]
        WHERE id = ? and nombre = ? and fecha_nacimiento = ?
    """
    
    params = [cliente.id, cliente.nombre ,cliente.fecha_nacimiento]

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

async def delete_cliente(id: int) -> str:

    deletescript = """
       DELETE FROM [FARMACIA].[CLIENTE]
       WHERE [id] = ?
    """

    params = [id];
     
    try:
        result = await execute_query_json(deletescript, params=params,needs_commit=True)
        return "DELETED"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")

async def update_cliente(cliente:cliente) -> cliente:


    dict = cliente.model_dump(exclude_none = True)

    keys = [k for k in dict.keys()]
    keys.remove('id')
    variables = " = ?, ".join(keys)+ " = ?"

    updatescript = f"""
        UPDATE [FARMACIA].[CLIENTE]
        SET {variables}
        WHERE [id] = ?;
    """
    params = [dict[v] for v in keys]
    params.append(cliente.id)

    update_result = None
    try:
        result = await execute_query_json(updatescript, params=params,needs_commit=True)
        return "Informacion Actualizada"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")
    
    sqlfind: str = """
        SELECT [id]
            ,[nombre]
            ,[fecha_nacimiento]
        FROM [FARMACIA].[CLIENTE]
        WHERE id = ? and nombre = ? and fecha_nacimiento = ?
    """
    
    params = [cliente.id, cliente.nombre ,cliente.fecha_nacimiento]

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

async def delete_cliente(id: int) -> str:

    deletescript = """
       DELETE FROM [FARMACIA].[CLIENTE]
       WHERE [id] = ?
    """

    params = [id];
     
    try:
        result = await execute_query_json(deletescript, params=params,needs_commit=True)
        return "DELETED"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")
