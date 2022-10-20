from api_config import db
from graphene import (
    ObjectType,
    Mutation,
    Int,
    String,
    Field,
)
from .objects import (
    Funko,
    User,
)
from .funko import Funko as FunkoModel
from .user import User as UserModel


class createFunko(Mutation):
    class Arguments:
        number = Int(required=True)
        name = String(required=True)
        collection = String(required=True)

    funko = Field(lambda: Funko)

    def mutate(self, info, number, name, collection):
        funko = FunkoModel(number=number, name=name, collection=collection)
        db.session.add(funko)
        db.session.commit()

        return createFunko(funko=funko)


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
        funko_id = Int()

    user = Field(lambda: User)

    def mutate(self, info, id, first_name=None, last_name=None, funko_id=None):
        user = UserModel.query.get(id)
        if user:
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if funko_id:
                user.funko_id = funko_id
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
    create_funko = createFunko.Field()
    create_user = createUser.Field()
    update_user = updateUser.Field()
    delete_user = deleteUser.Field()