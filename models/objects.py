from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
)
from graphene import (
    Int
)
from models.funko import Funko as FunkoModel
from models.user import User as UserModel

class Funko(SQLAlchemyObjectType):
    class Meta:
        model = FunkoModel
    number = Int(description='the number of the funko pop')


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ('funko_id', 'last_name', )