from unittest import TestCase
from api.controllers import MutantController


class TestMutantController(TestCase):

    def setUp(self):
        self.dna = ['ATGCGA',
                    'CAGTGC',
                    'TTATGT',
                    'AGAAGG',
                    'CCCCTA',
                    'TCACTG']

    def test_is_mutant(self):
        dna = ['TCACTG',
                'TCACGG',
                'TCAGTG',
                'TCGCTG',
                'TCACTG',
                'TCACTG']

        mc = MutantController()
        self.assertTrue(mc.is_mutant(self.dna))

    def test__decompose_dna(self):
        mc = MutantController()
        mc._decompose_dna(self.dna)

    def test__decompose_vertically(self):
        mc = MutantController()
        vertical_sequences = mc._decompose_vertically(self.dna)
        self.assertEqual(6, len(vertical_sequences))
        self.assertEqual('ACTACT', vertical_sequences[0])
        self.assertEqual('TATGCC', vertical_sequences[1])
        self.assertEqual('GGAACA', vertical_sequences[2])
        self.assertEqual('CTTACC', vertical_sequences[3])
        self.assertEqual('GGGGTT', vertical_sequences[4])
        self.assertEqual('ACTGAG', vertical_sequences[5])

    def test__decompose_lower_diagonals(self):
        mc = MutantController()
        diagonal_sequences = mc._decompose_lower_diagonals(self.dna[1:])
        self.assertEqual(5, len(diagonal_sequences))
        self.assertEqual('CTACT', diagonal_sequences[0])
        self.assertEqual('TGCC', diagonal_sequences[1])
        self.assertEqual('ACA', diagonal_sequences[2])
        self.assertEqual('CC', diagonal_sequences[3])
        self.assertEqual('T', diagonal_sequences[4])

    def test__decompose_upper_diagonals(self):
        dna = ['ATGCGA',
               'CAGTGC',
               'TTATGT',
               'AGAAGG',
               'CCCCTA',
               'TCACTG']

        mc = MutantController()
        diagonal_sequences = mc._decompose_upper_diagonals([x[1:] for x in dna[:-1]])
        self.assertEqual(5, len(diagonal_sequences))
        self.assertEqual('TGTGA', diagonal_sequences[0])
        self.assertEqual('GTGG', diagonal_sequences[1])
        self.assertEqual('CGT', diagonal_sequences[2])
        self.assertEqual('GC', diagonal_sequences[3])
        self.assertEqual('A', diagonal_sequences[4])

    def test__decompose_middle_diagonals(self):
        mc = MutantController()
        vertical_sequences = mc._decompose_middle_diagonal(self.dna)
        self.assertEqual(6, len(vertical_sequences))
        self.assertEqual('AAAATG', vertical_sequences)

    def test__reverse_sequences(self):
        mc = MutantController()
        reversed_aequences = mc._reverse_sequences(self.dna)
        self.assertEqual(6, len(reversed_aequences))
        self.assertEqual('AGCGTA', reversed_aequences[0])
        self.assertEqual('CGTGAC', reversed_aequences[1])
        self.assertEqual('TGTATT', reversed_aequences[2])
        self.assertEqual('GGAAGA', reversed_aequences[3])
        self.assertEqual('ATCCCC', reversed_aequences[4])
        self.assertEqual('GTCACT', reversed_aequences[5])

    def test__decompose_diagonally(self):
        mc = MutantController()
        diagonal_sequences = mc._decompose_diagonally(self.dna)
        self.assertEqual(11, len(diagonal_sequences))
        self.assertEqual('AAAATG', diagonal_sequences[0])
        self.assertEqual('CTACT', diagonal_sequences[1])
        self.assertEqual('TGCC', diagonal_sequences[2])
        self.assertEqual('ACA', diagonal_sequences[3])
        self.assertEqual('CC', diagonal_sequences[4])
        self.assertEqual('T', diagonal_sequences[5])
        self.assertEqual('TGTGA', diagonal_sequences[6])
        self.assertEqual('GTGG', diagonal_sequences[7])
        self.assertEqual('CGT', diagonal_sequences[8])
        self.assertEqual('GC', diagonal_sequences[9])
        self.assertEqual('A', diagonal_sequences[10])

    def test__decompose_diagonally_but_backwards(self):
        mc = MutantController()
        diagonal_sequences = mc._decompose_diagonally_but_backwards(self.dna)
        self.assertEqual(11, len(diagonal_sequences))
        self.assertEqual('AGTACT', diagonal_sequences[0])
        self.assertEqual('CGACC', diagonal_sequences[1])
        self.assertEqual('TGCA', diagonal_sequences[2])
        self.assertEqual('GTC', diagonal_sequences[3])
        self.assertEqual('AT', diagonal_sequences[4])
        self.assertEqual('G', diagonal_sequences[5])
        self.assertEqual('GTAGC', diagonal_sequences[6])
        self.assertEqual('CGTA', diagonal_sequences[7])
        self.assertEqual('GAT', diagonal_sequences[8])
        self.assertEqual('TC', diagonal_sequences[9])
        self.assertEqual('A', diagonal_sequences[10])

    def test_verify_one_found_mutant_sequence(self):
        mc = MutantController()
        self.assertEqual(1, mc._verify_mutant_sequence('CCCCTA'))

    def test_verify_two_found_mutant_sequence(self):
        mc = MutantController()
        self.assertEqual(2, mc._verify_mutant_sequence('CCCCTTTTA'))

    def test_verify_zero_found_mutant_sequence(self):
        mc = MutantController()
        self.assertEqual(0, mc._verify_mutant_sequence('CCACCTTATT'))

    def test_verify_many_found_mutant_sequence(self):
        mc = MutantController()
        self.assertEqual(0, mc._verify_mutant_sequence('CCACCTTATT'))
        self.assertEqual(1, mc._verify_mutant_sequence('CCCCTA'))
        self.assertEqual(2, mc._verify_mutant_sequence('CCCCTTTTA'))
        self.assertEqual(4, mc._verify_mutant_sequence('CCCCTACCCCTACCCCTTTTA'))

    def test_verify_zero_found_mutant_short_sequence(self):
        mc = MutantController()
        self.assertEqual(0, mc._verify_mutant_sequence('CCA'))
        self.assertEqual(0, mc._verify_mutant_sequence('CCAA'))
        self.assertEqual(0, mc._verify_mutant_sequence('C'))
        self.assertEqual(0, mc._verify_mutant_sequence(''))

    def test__validate_corrupt_dna(self):
        mc = MutantController()
        dna = ["ATGCG", "CAGTGC", "TTGTCT", "AGAAGG", "CCACTA", "TCACTG"]
        with self.assertRaises(ValueError):
            mc._validate_dna(dna)

    def test__validate_corrupt_dna_sequence(self):
        mc = MutantController()
        dna = ["ATGCGA", "CAGTGC", "TTGTCT", "AGAAKG", "CCACTA", "TCACTG"]
        with self.assertRaises(ValueError):
            mc._validate_dna(dna)

