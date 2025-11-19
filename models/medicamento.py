from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date
import re


class medicamento(BaseModel):
    id: Optional[int] = Field(
        default=None,
        description="El ID autoincrementable para medicamento"
    )

    nombre: Optional[str] = Field(
        description="Nombre: medicamentto",
        pattern=r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ' -]+$",
        default=None,
        examples=["Amoxicilina"]
    )

    fecha_vencimiento: Optional[date] = Field(
        description="2000-04-21"
    )

