from app.conta_vogais import conta_vogais

def test_verifica_se_a_contagem_de_vogais_esta_correta():
    assert conta_vogais('macarrao') == 4
    assert conta_vogais('lucas') == 2
    assert conta_vogais('macaco') == 3