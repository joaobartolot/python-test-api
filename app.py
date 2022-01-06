import os

from flask import Flask
from flask_restful import Api

from api.controller.v1.cpf_controller import CPFController

app = Flask(__name__)
api = Api(app)

api.add_resource(CPFController, '/<string:cpf>/')

if __name__ == '__main__':
    app.run(debug=True)
