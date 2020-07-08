from main import app
import unittest
import json
from http import HTTPStatus
from api.utils import uris


class TestMutant(unittest.TestCase):

    def setUp(self) -> None:
        self.api = app
        self.client = self.api.test_client()
        self.content_type = 'application/json'

    def test__true_mutant(self):
        resp = self.client.post(path=uris.MUTANT_URI,
                                content_type=self.content_type,
                                data=json.dumps(
            {
                "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"
                ]
            }
        ))
        self.assertEqual(resp.status_code, HTTPStatus.OK)

    def test__false_mutant(self):
        resp = self.client.post(path=uris.MUTANT_URI,
                                content_type=self.content_type,
                                data=json.dumps(
            {
                "dna": ["ATGCGA", "CAGTGC", "TTGTCT", "AGAAGG", "CCACTA", "TCACTG"
                ]
            }
        ))
        self.assertEqual(resp.status_code, HTTPStatus.FORBIDDEN)

    def test__corrupt_dna(self):
        resp = self.client.post(path=uris.MUTANT_URI,
                                content_type=self.content_type,
                                data=json.dumps(
            {
                "dna": [
                    "ATGCG", "CAGTGC", "TTGTCT", "AGAAGG", "CCACTA", "TCACTG"
                ]
            }
        ))
        self.assertEqual(resp.status_code, HTTPStatus.BAD_REQUEST)

    def test__corrupt_dna_sequence(self):
        resp = self.client.post(path=uris.MUTANT_URI,
                                content_type=self.content_type,
                                data=json.dumps(
            {
                "dna": ["ATGCGK", "CAGTGC", "TTGTCT", "AGAAGG", "CCACTA", "TCACTG"
                ]
            }
        ))
        self.assertEqual(resp.status_code, HTTPStatus.BAD_REQUEST)


if __name__ == '__main__':
    unittest.main()
