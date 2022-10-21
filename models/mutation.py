from itertools import product
from numbers import Real
from tokenize import Double
from typing_extensions import Required
from unicodedata import category
from api_config import db
from graphene import (
    ObjectType,
    Mutation,
    Int,
    String,
    Field,
)
from .objects import (
    Producto,
    User,
)
from .product import Product as ProductModel
from .user import User as ProdcutModel


class createProduct(Mutation):
    class Arguments:
        number = Int(required=True)
        name = String(required=True)
        precio = float(required=True)
        stock = Int(required=True)
        descripcion = String (required=True)
        categoria = String(required=True)

    product = Field(lambda: Producto)

    def mutate(self, info, number, name, precio, stock, descripcion, categoria):
        funko = ProductModel(number=number, name=name, precio=precio, stock=stock, descripcion=descripcion, categoria=categoria)
        db.session.add(product)
        db.session.commit()

        return createProduct(product=product)


class createUser(Mutation):
    class Arguments:
        first_name = String(required=True)
        last_name = String(required=True)

    user = Field(lambda: User)

    def mutate(self, info, first_name, last_name):
        user = UserModel(first_name=first_name, last_name=last_name)
        db.session.add(user)
        db.session.commit()

        return createUser(user=user)

class updateUser(Mutation):
    class Arguments:
        id = Int(required=True)
        first_name = String()
        last_name = String()
        product_id = Int()

    user = Field(lambda: User)

    def mutate(self, info, id, first_name=None, last_name=None, product_id=None):
        user = UserModel.query.get(id)
        if user:
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if product_id:
                user.product_id = product_id
            db.session.add(user)
            db.session.commit()

        return updateUser(user=user)

class deleteUser(Mutation):
    class Arguments:
        id = Int(required=True)

    user = Field(lambda: User)

    def mutate(self, info, id):
        user = UserModel.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()

        return deleteUser(user=user)

class Mutation(ObjectType):
    create_product= createProduct.Field()
    create_user = createUser.Field()
    update_user = updateUser.Field()
    delete_user = deleteUser.Field()