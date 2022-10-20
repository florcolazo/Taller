from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
)
from graphene import (
    Int
)
from models.product import Product as ProductCategoty
from models.user import User as UserModel

class Producto(SQLAlchemyObjectType):
    class Meta:
        model = ProductCategoty
    number = Int(description='the number of the product')


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ('product_id', 'name', )