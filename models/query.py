from graphene import (
    ObjectType,
    String,
    relay,
    # Field,
    List,
    Int
)

# from models import (
#     funko,
#     persona,
# )
from .product import Product as ProductModel
from .objects import (
    Product,
    User,
)




class Query(ObjectType):
    productos = List(lambda: Funko, collection=String(), name=String())
    # funkos = List(lambda: Funko, collection=String(), name=String())
    users = List(lambda: User)

    def resolve_funkos(self, info, collection=None, name=None):
        query = Funko.get_query(info=info)
        if collection:
            query = query.filter(FunkoModel.collection == collection)
        if name:
            query = query.filter(FunkoModel.name == name)
        return query.all()

    def resolve_users(self, info):
        query = User.get_query(info=info)
        return query.all()
    # def resolve_funkos(self, info, collection=None, name=None):
    #     query = Funko.get_query(info=info)
    #     #    query = query.filter(SkillModel.profile_id == self.id)
    #     if collection:
    #         query = query.filter(funko.Funko.collection == collection)
    #     if name:
    #         query = query.filter(funko.Funko.name == name)

    #     return query.all()

    # def resolve_personas(self, info):
    #     query = Persona.get_query(info=info)
    #     #    query = query.filter(SkillModel.profile_id == self.id)
    #     #    if name:
    #     #        query = query.filter(SkillModel.name == name)
    #     #    if score:
    #     #        query = query.filter(SkillModel.score == score)

    #     return query.order_by('id').all()