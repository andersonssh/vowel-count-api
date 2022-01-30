swagger_config = {
        "headers": [],
        "specs": [{
            "endpoint": "/apispec_1",
            "route": '/api/',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True}
        ],
        "basePath": "/",
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs",
    }
swagger_template = {
        "swagger": '2.0',
        "operationId": "getmyData",
        "info": {
            "title": "Contador de Vogais",
            "description": "API contadora de vogais",
            "version": "2.0",
            "basePath": "localhost:5000/api/",
        }
    }