from flask import request
from flask_restful import Resource
from api.controllers import MutantController
from http import HTTPStatus
from flask_restful import abort


class MutantAPI(Resource):

    def post(self):
        try:
            json_data = request.get_json()
            self._validate_post_request(json_data)
            mc = MutantController()
            if mc.is_mutant(json_data.get("dna")):
                response = {}, HTTPStatus.OK
            else:
                response = {}, HTTPStatus.FORBIDDEN
            return response
        except ValueError as e:
            abort(HTTPStatus.BAD_REQUEST)
        except Exception as e:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    def _validate_post_request(self, json_data):
        if json_data is None or not isinstance(json_data.get("dna"), list):
            abort(HTTPStatus.BAD_REQUEST)



class StatsAPI(Resource):

    def get(self):
        json_data = request.json()
