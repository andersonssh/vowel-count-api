# Contador de vogais
API que devolve a quantidade de vogais de cada palavra apartir de uma lista de palavras.

## Requisitos básicos
* Python3.x
```bash
$ sudo apt install python3 
```
* venv
```bash
$ sudo apt install python3-venv 
```

## Executar o aplicativo
1. Clonar o repositório e entrar na pasta do projeto
```bash
$ git clone https://github.com/andersonssh/contador-de-vogais
$ cd contador-de-vogais
```
2. Configurar ambiente virtual
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```
3. Instalar dependências
```bash 
$ pip install -r requirements.txt
  ```
4. Executar a aplicação
```bash 
$ python3 main.py
```
5. Endereço da aplicação:
https://localhost:5000

Você pode enviar requisições partir do navegador acessando a rota exibida no tópico abaixo.

## Documentação
A documentação foi construida utilizando Swagger e pode ser acessada no endereço:
http://localhost:5000/docs

## Testes
Para executar todos os testes digite o comando:
```bash
$ pytest testes/
```

## Estrutura de arquivos

```bash
.
├── app
│   ├── conta_vogais.py
│   ├── docs
│   │   ├── configuracoes.py
│   │   ├── contador_vogais.yaml
│   ├── __init__.py
├── main.py
├── README.md
├── requirements.txt
├── testes
│   ├── funcional
│   │   ├── __init__.py
│   │   └── test_app.py
│   ├── __init__.py
│   └── unitario
│       ├── __init__.py
│       └── test_conta_vogais.py
```

## Endpoints
* http://localhost:5000/vowel_count