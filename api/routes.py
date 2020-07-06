from flask import request
from flask_restful import Resource
from api.controllers import MutantController
from http import HTTPStatus


class MutantAPI(Resource):

    def post(self):
        json_data = request.get_json()
        mc = MutantController(json_data)
        if mc.is_mutant():
            response = {}, HTTPStatus.OK
        else:
            response = {}, HTTPStatus.FORBIDDEN
        return response


class StatsAPI(Resource):

    def get(self):
        json_data = request.json()
