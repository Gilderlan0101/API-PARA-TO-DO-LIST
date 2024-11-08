from flask import Flask
from flask_restx import Api


class Servidor:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            version='1.0',
            title='To do list API',
            description='Api que gerencia toda nosso site de to do list sem banco de dados'
        )

servidor = Servidor()  # Esta linha cria a instância do servidor
