class MutantController:

    def __init__(self, dna):
        self._dna = dna

    def is_mutant(self):
        print(self._dna)
        dna_list = self._dna.get("dna")
        print("".join(dna_list))


