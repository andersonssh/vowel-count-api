from flask import Flask
from flask_restful import Api
from app.conta_vogais import VogaisPorPalavra


app = Flask(__name__)
api = Api(app)

api.add_resource(VogaisPorPalavra, '/vowel_count')

if __name__ == '__main__':
    app.run(debug=True)