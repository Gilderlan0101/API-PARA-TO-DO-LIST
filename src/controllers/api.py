from flask_restx import Resource

from src.server.services import servidor
from src.models.model import entrada

app, api = servidor.app, servidor.api



class TaskCrud(object):
    def __init__(self):
        self.count = 0
        self.tasks = []


    def get(self, id):
        for task in self.tasks:
            if task['id'] == id:
                return task
        api.abort(404, "A task do id { } não existe".format(id))

    
    def create(self, data):
        task = data
        task['id'] = self.count = self.count + 1
        self.tasks.append(task)
        return task

    
    def update(self, data, id):
        task = self.get(id)
        task.update(data)
        return task

    
    def delete(self, id):
        task = self.get(id)
        self.tasks.remove(task)

task = TaskCrud()


@api.route("/task")
class ListTask(Resource):
    """Exibir todas as tarefas"""

    @api.doc("Exibindo todas as tarefas")
    @api.marshal_with(entrada)
    def get(self):
        return task.tasks
    

    @api.doc("Adicionando uma nova tarefa..")
    @api.expect(entrada, validate=True)
    @api.marshal_with(entrada, code=201)
    def post(self):

        return task.create(api.payload), 201
    


@api.route("/task/<int:id>")
@api.response(404, "task não encontrada")
@api.param('id', 'O identificado da task')
class Task(Resource):
    

    """Mostra uma única tarefa e permite deletá-la pelo ID"""
    @api.doc('get nas task')
    @api.marshal_list_with(entrada)
    def get(self, id):
        """Lista uma task pelo seu id"""

        return task.get(id)


    @api.doc('Deleta uma task')
    @api.response(204, 'task deletada')
    def delete(self, id):

        task.delete(id)
        return '', 204
