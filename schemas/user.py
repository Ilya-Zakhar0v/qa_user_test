from pydantic import BaseModel, Field, validator, EmailStr, conint
from typing import TypeVar

T = TypeVar('T', bound=BaseModel)


class CreateUserModel(BaseModel):
    code: int = Field(..., description="Код ответа API")
    type: str = Field(...)
    message: str = Field(..., description="Сообщение ответа")

    @validator("code")
    def valid(cls, code):
        if code != 200:
            raise ValueError("error code validation")
        else:

            return code


class UpdateUserModel(BaseModel):
    code: int = Field(..., description="Код ответа API")
    type: str = Field(...)
    message: str = Field(..., description="Сообщение ответа")

    @validator("code")
    def valid(cls, code):
        if code != 200:
            raise ValueError("error code validation")
        else:
            return code
    


