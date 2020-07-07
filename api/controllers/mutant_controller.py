import re


class MutantController:

    MUTANT_SEQUENCE_SIZE = 4
    MINIMUM_MUTANTS_SEQUENCES = 1

    def is_mutant(self, dna):
        is_mutant = False
        self._validate_dna(dna)
        sequences = self._decompose_dna(dna)
        count = self._count_mutant_sequences(sequences)
        if count > self.MINIMUM_MUTANTS_SEQUENCES:
            is_mutant = True
        return is_mutant

    def _validate_dna(self, dna):
        is_valid = False
        dna_size = len(dna)
        for seq in dna:
            if len(seq) != dna_size:
                raise ValueError("The DNA sequence is corrupt")
            x = re.findall("[^ATCG]", seq, re.IGNORECASE)
            if x:
                raise ValueError("The Nitrogen base corrupt")

        return is_valid

    def _decompose_dna(self, dna):
        sequences = []
        sequences.extend(dna)
        sequences.extend(self._decompose_vertically(dna))
        sequences.extend(self._decompose_diagonally(dna))
        sequences.extend(self._decompose_diagonally_but_backwards(dna))
        return sequences

    @staticmethod
    def _decompose_vertically(dna):
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

