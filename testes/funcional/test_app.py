import pytest
from main import app
import json


@pytest.fixture(scope='module')
def client():
    # executando modo de teste do flask
    app.config['TESTING'] = True
    # criando o contexto
    context = app.app_context()
    # executa o contexto
    context.push()
    # retorna gerador do client
    yield app.test_client()
    # remove contexto
    context.pop()

def test_verifica_resposta_da_rota_que_conta_vogais(client):
    # enviando requisicao
    resposta_requisicao = client.post('/vowel_count', json=['josé', 'meio', 'sofá'])

    # convertendo resposta da requisicao para json
    resposta = resposta_requisicao.data.decode('utf8').replace('\n', '')
    json_resposta = json.loads(resposta)

    # verificando se a resposta da requisicao esta correta
    assert json_resposta == {'josé': 2, 'meio': 3, 'sofá': 2}
