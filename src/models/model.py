from flask_restx import fields
from src.server.services import servidor


entrada = servidor.api.model('API', {
    'id': fields.Integer(readonly=True, description='Das task serão automáticas'),
    'task': fields.String(required=True, description='Adicione uma nova task aqui.')
})
