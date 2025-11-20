from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date
import re


class cliente(BaseModel):
    id: Optional[int] = Field(
        default=None,
        description="El ID autoincrementable para medicamento"
    )

    nombre: Optional[str] = Field(
        description="Nombre: ",
        pattern=r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ' -]+$",
        default=None,
        examples=["Jose"]
    )

    fecha_nacimiento: Optional[date] = Field(
        default=None,
        description="2000-04-21"
    )

