from fastapi_tdd.models.base import CreateBaseModel
from fastapi_tdd.schemas.product import ProductIn


class ProductModel(ProductIn, CreateBaseModel):
    ...
