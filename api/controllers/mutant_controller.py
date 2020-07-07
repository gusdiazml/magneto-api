class MutantController:
    MUTANT_SEQUENCE_SIZE = 4

    def __init__(self, dna):
        self._dna = dna

    def is_mutant(self):
        is_mutant = False
        sequences = self._decompose_dna()
        count = self._count_mutant_sequences(sequences)
        print("cantidad de mutantes: ", count)
        if count > 1:
            is_mutant = True
        return is_mutant

    def _decompose_dna(self):
        sequences = []
        sequences.extend(self._dna)
        sequences.extend(self._decompose_vertically(self._dna))
        sequences.extend(self._decompose_diagonally(self._dna))
        sequences.extend(self._decompose_diagonally_but_backwards(self._dna))
        return sequences

    def _decompose_vertically(self, dna):
        dna_vertors_len = len(dna)
        vertical_sequences = []
        for i in range(dna_vertors_len):
            temporal_vertical_seq = ""
            for sequences in dna:
                temporal_vertical_seq += sequences[i]

            vertical_sequences.append(temporal_vertical_seq)
        return vertical_sequences

    def _decompose_diagonally(self, dna):
        sequences = []
        middle_diagonal = self._decompose_middle_diagonal(dna)
        down_diagonals = self._decompose_lower_diagonals(dna[1:])
        upper_diagonals = self._decompose_upper_diagonals([x[1:] for x in dna[:-1]])
        sequences.append(middle_diagonal)
        sequences.extend(down_diagonals)
        sequences.extend(upper_diagonals)
        return sequences

    def _decompose_middle_diagonal(self, dna):
        temp_sequence = ""
        for i, seq in enumerate(dna):
            temp_sequence += seq[i]
        return temp_sequence

    def _decompose_upper_diagonals(self, dna):
        diagonal_list = [self._decompose_middle_diagonal(dna)]
        if len(dna) > 1:
            diagonal_list.extend(self._decompose_upper_diagonals([x[1:] for x in dna[:-1]]))
        return diagonal_list

    def _decompose_lower_diagonals(self, dna):
        diagonal_list = [self._decompose_middle_diagonal(dna)]
        if len(dna) > 1:
            diagonal_list.extend(self._decompose_lower_diagonals(dna[1:]))
        return diagonal_list

    def _decompose_diagonally_but_backwards(self, dna):
        reversed_dna = self._reverse_sequences(dna)
        return self._decompose_diagonally(reversed_dna)

    def _reverse_sequences(self, sequences):
        reversed_sequences = []
        for sequence in sequences:
            reversed_sequences.append("".join(reversed(sequence)))
        return reversed_sequences

    def _count_mutant_sequences(self, sequences):
        verified_mutant_sequences_count = 0
        for sequence in sequences:
            verified_mutant_sequences_count += self._verify_mutant_sequence(sequence)
        return verified_mutant_sequences_count

    def _verify_mutant_sequence(self, sequence):
        found_base_count = 0
        sequences_found = 0
        last_base = None
        sequence_len = len(sequence)
        if sequence_len >= self.MUTANT_SEQUENCE_SIZE:
            for i, base in enumerate(sequence):
                if i == 0:
                    last_base = base
                    continue
                if last_base == base:
                    found_base_count += 1
                else:
                    found_base_count = 0
                if found_base_count == self.MUTANT_SEQUENCE_SIZE - 1:
                    sequences_found += 1
                    found_base_count = 0
                last_base = base
        return sequences_found

