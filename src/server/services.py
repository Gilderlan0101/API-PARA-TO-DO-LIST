from flask import Flask
from flask_restx import Api

import os

class Servidor:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            version='1.0',
            title='To do list API',
            description='Api que gerencia toda nosso site de to do list sem banco de dados'
        )

    def run(self):
        self.app.run(
            host='0.0.0.0',  # Aceitar conexões externas
            port=int(os.environ.get("PORT", 5000)),  # Usar a porta do Render ou 5000
            debug=True
        )

servidor = Servidor()