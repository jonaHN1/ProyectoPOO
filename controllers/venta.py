
from datetime import datetime
import json
import logging

from fastapi import HTTPException

from models.venta import venta
from utils.database import execute_query_json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



async def crear_venta( venta: venta ) -> venta:

    sqlscript: str = """
        INSERT INTO [FARMACIA].[VENTA] ([id])
        VALUES (?);
    """

    params = [
        venta.id,
    ]

    insert_result = None
    try:
        insert_result = await execute_query_json( sqlscript, params, needs_commit=True )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")

    sqlfind: str = """
        SELECT [id]
        FROM [FARMACIA].[VENTA]
        WHERE id = ? 
    """
    
    params = [venta.id]

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




