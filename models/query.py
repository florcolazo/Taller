from graphene import (
    ObjectType,
    String,
    relay,
    # Field,
    List,
    Int
)


from .product import Product as ProductModel
from .objects import (
    Product,
    User,
)




class Query(ObjectType):
    productos = List(lambda: Funko, collection=String(), name=String())
    users = List(lambda: User)

    def resolve_product(self, info, collection=None, name=None):
        query = Product.get_query(info=info)
        if collection:
            query = query.filter(ProductModel.collection == collection)
        if name:
            query = query.filter(FunkoModel.name == name)
        return query.all()

    def resolve_users(self, info):
        query = User.get_query(info=info)
        return query.all()
