from flask import Flask
from flask_restful import Api
from app.conta_vogais import VogaisPorPalavra
from flasgger import Swagger
from app.docs import configuracoes

app = Flask(__name__)
api = Api(app)
flasgger = Swagger(app,
                   config=configuracoes.swagger_config,
                   template=configuracoes.swagger_template,
                   )

api.add_resource(VogaisPorPalavra, '/vowel_count')

if __name__ == '__main__':
    app.run(debug=True)