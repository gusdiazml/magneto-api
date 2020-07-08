from flask import request
from flask_restful import Resource
from http import HTTPStatus
from flask_restful import abort
from werkzeug.exceptions import BadRequest



class MutantAPI(Resource):

    def post(self):
        try:
            from api.controllers import MutantController
            json_data = request.get_json()
            self._validate_post_request(json_data)
            mc = MutantController()
            is_mutant = mc.is_mutant(json_data.get("dna"))
            if is_mutant:
                response = {}, HTTPStatus.OK
            else:
                response = {}, HTTPStatus.FORBIDDEN
            return response
        except ValueError as e:
            abort(HTTPStatus.BAD_REQUEST)
        except BadRequest:
            abort(HTTPStatus.BAD_REQUEST)
        except Exception as e:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    def _validate_post_request(self, json_data):
        if json_data is None or not isinstance(json_data.get("dna"), list):
            abort(HTTPStatus.BAD_REQUEST)


class StatsAPI(Resource):

    def get(self):
        try:
            from api.controllers import MutantController
            response = MutantController.get_stats()
            return response, HTTPStatus.OK
        except Exception as e:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR)

