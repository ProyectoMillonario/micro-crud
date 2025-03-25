from pydantic import BaseModel

class Token(BaseModel):
    """Clase para devolver el token y el tipo de token

    Args:
        BaseModel (_type_): _description_
    """
    access_token: str
    token_type: str