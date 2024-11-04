API To-Do List

Bem-vindo à API To-Do List! Esta é uma API RESTful desenvolvida em Python usando o Flask e o Flask-RESTx, criada para permitir a criação, visualização, edição e remoção de tarefas. Ela está disponível para todos que desejam utilizá-la, estudar seu código, e aprender como construir uma API com Flask.
Funcionalidades

A API oferece os seguintes endpoints:

    GET /task: Retorna todas as tarefas.
    POST /task: Cria uma nova tarefa.
    GET /task/{id}: Retorna uma tarefa específica pelo seu ID.
    PUT /task/{id}: Atualiza uma tarefa existente pelo ID.
    DELETE /task/{id}: Deleta uma tarefa específica pelo ID.

Tecnologias Utilizadas

    Flask: Microframework para aplicações web em Python.
    Flask-RESTx: Extensão do Flask para criar APIs RESTful com documentação integrada.
    Python 3: A linguagem principal para este projeto.

Instalação e Configuração

Para rodar a API localmente, siga os passos abaixo:
1. Clone este repositório:

bash

git clone https://github.com/Gilderlan0101/API-PARA-TO-DO-LIST.git
cd API-PARA-TO-DO-LIST

2. Crie um ambiente virtual e ative-o:

bash

python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências:

bash

pip install -r requirements.txt

4. Inicie a aplicação:

bash

python app.py

A API estará disponível em http://127.0.0.1:5000.
Endpoints e Exemplos de Uso
Criar uma Tarefa (POST)

    Endpoint: /task
    Método: POST
    Parâmetros: { "task": "Nome da Tarefa" }

Exemplo de requisição usando curl:

bash

curl -X POST http://127.0.0.1:5000/task -H "Content-Type: application/json" -d '{"task": "Nova Tarefa"}'

Listar Todas as Tarefas (GET)

    Endpoint: /task
    Método: GET

Exemplo de requisição usando curl:

bash

curl http://127.0.0.1:5000/task

Deletar uma Tarefa (DELETE)

    Endpoint: /task/{id}
    Método: DELETE
    Parâmetros: id da tarefa a ser deletada.

Exemplo de requisição usando curl:

bash

curl -X DELETE http://127.0.0.1:5000/task/1

Contribuição

Este projeto é aberto e livre para todos usarem e estudarem. Se desejar contribuir, sinta-se à vontade para fazer um fork do repositório, adicionar suas melhorias e enviar um pull request.
Licença

Este projeto é de uso livre, e todos são bem-vindos para usá-lo e estudá-lo.
