from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date
import re


class venta(BaseModel):
    id: Optional[int] = Field(
        default=None,
        description="Ingrese un numero de venta"
    )

