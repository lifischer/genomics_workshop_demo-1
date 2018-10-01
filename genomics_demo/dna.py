complimentary_nucleotides = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


class DNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
        if not self._check_validity():
            raise ValueError("Bad sequence. Sequences must only contain G, C, A, and T")

    def __eq__(self, other):
        return True if str(self) == str(other) else False

    def __str__(self):
        return self.sequence

    def __repr__(self):
        return "DNA(sequence='{}')".format(self.sequence)

    def _check_validity(self):
        return all(nucleotide in 'GCAT' for nucleotide in self.sequence.upper())

    @property
    def complimentary_sequence(self):
        return DNA(''.join(complimentary_nucleotides[nt.upper()] for nt in self.sequence))


    def gc_content(self):
        return 0.5
        #gc_count = self.count("G") + self.count("C")
        #gc_fraction = float(gc_count) / len(self)
        #return 100 * gc_fraction



    @property
    def split_DNA_triplets(self):
        """
        This functions divides DNA sequence into triplets, irrespective of where the start codon is.
        """
        return [self.sequence[i:i + 3] for i in range(0, len(self.sequence), 3)]

    @property
    def find_first_start_site(self):
        '''
        Seeks position of the first start codon, if present.
        '''
        for i in range(0,len(self.sequence)):
            if self.sequence[i:i + 3] == 'ATG':
                return i
        raise TypeError("No start codon found")

