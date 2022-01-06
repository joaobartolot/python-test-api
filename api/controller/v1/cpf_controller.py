from flask_restful import Resource, abort
from werkzeug.exceptions import BadRequest

from api.service.cpf_service import CPFService


class CPFController(Resource):
    def get(self, cpf):
        service = CPFService(cpf)

        if not service.validar():
            raise BadRequest(
                "O CPF e invalido, porfavor verifique se o formato digitado e: '00000000000'")

        if not service.verificar_blacklist():
            return {"status": "BLOCK"}

        return {"status": "FREE"}
