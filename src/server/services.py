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

    def run(self):
        self.app.run(
           
        )


servidor = Servidor()