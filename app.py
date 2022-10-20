#docker ps --INSTALAR BASE DE DATOS POSTGRESS
#docker run
#postman-api backaup-descargar GET LOCAL HOST 50000-CADA DATO ES UNA TUPLA
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"




from api_config import (
    app,
    db,
)

from models.schema import schema
from flask_graphql import GraphQLView

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  #? Habilita la interfaz GraphiQL
    )
)

if __name__ == "__main__":
    app.run(port=5000, host='localhost')