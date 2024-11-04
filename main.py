from src.server.services import servidor
from src.controllers.api import *


app = servidor.app 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
