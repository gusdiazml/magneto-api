import unittest
from api.controllers.mutant_controller import MutantController


class MutantControllerTest(unittest.TestCase):

    def test_is_mutant_true(self):
        dna = {'dna': ['ATGCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG']}
        mc = MutantController(dna)
        self.assertTrue(mc.is_mutant())



if __name__ == '__main__':
    unittest.main()
