from flask import request
from flask_restful import Resource
from flasgger import swag_from
import unidecode


def conta_vogais(string:str) -> int:
    """
    Pega a quantidade de vogais presentes em uma string
    :param string: str: String para análise
    :return: int: Inteiro com a quantidade de vogais encontradas
    """
    # todas as vogais
    vogais = ['a', 'e', 'i', 'o', 'u']
    # calcula e retorna a quantidade de vogais
    return len([letra for letra in unidecode.unidecode(string.lower()) if letra in vogais])


class VogaisPorPalavra(Resource):
    @swag_from('docs/contador_vogais.yaml')
    def post(self):
        # declaracão de dicionário que recebe todas as
        # palavras como chave e quantidade de vogais como valor
        vogais_por_palavra = {}

        try:
            # pega cada string dentro da lista enviada e a transforma em chave do dict
            for palavra in request.json:
                # chave - string | valor - quantidade de vogais | ex: ["leo"] -> {"leo": 2}
                vogais_por_palavra[palavra] = conta_vogais(palavra)
            # retorna dicionario
            return vogais_por_palavra, 200
        except AttributeError:
            # retorna mensagem de erro caso um item da lista nao seja uma string
            return {'message': 'apenas listas com strings são permitidas'}, 400
        except TypeError:
            # retorna mensagem de erro caso o objeto recebido nao seja uma lista
            return {'message': 'apenas listas são permitidas'}, 400