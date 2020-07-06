import unittest
from api import app
import json
from http import HTTPStatus

class TestMutant(unittest.TestCase):

    def setUp(self) -> None:
        self.api = app
        self.client = self.api.test_client()
        self.content_type = 'application/json'

    def test_mutant(self):
        resp = self.client.post(path='/mutant',
                                content_type=self.content_type,
                                data=json.dumps(
            {
                "dna": [
                    "ATGCGA",
                    "CAGTGC",
                    "TTATGT",
                    "AGAAGG",
                    "CCCCTA",
                    "TCACTG"
                ]
            }
        ))
        self.assertEqual(resp.status_code, HTTPStatus.OK)


if __name__ == '__main__':
    unittest.main()
