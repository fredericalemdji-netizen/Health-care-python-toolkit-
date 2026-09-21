"""
DNA/RNA sequence OOP pipeline (EXO 22-31)

Mixins (Loggable, Serializable), a Sequence base class, DNA/RNA
subclasses with complement logic, a timed-context-manager
experiment run, and a codon-reading iterator.

Extracted from exercise_of_level_intermediare.py — this was the
largest single block of live, working code in that file.
"""

import json
import logging
import time
from decimal import Decimal

logging.basicConfig(filename="min.log", level=logging.INFO)


class Loggable:
    def log(self, message):
        return logging.info(message)


class Serializable:
    def to_json(self):
        with open("pty.json", "w", newline="", encoding="utf-8") as f:
            json.dump(vars(self), f)


class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def length(self):
        return len(self.sequence)


class DNASequence(Sequence, Loggable, Serializable):
    def __init__(self, sequence):
        if not all(i in "ATGC" for i in sequence) and sequence != "":
            print("this isn't a dna sequence")
        super().__init__(sequence)

    def complement(self):
        structure = str.maketrans({"A": "T", "T": "A", "C": "G", "G": "C"})
        self.cDNA = self.sequence.translate(structure)
        return self.cDNA

    def present(self):
        print(f"the complementary DNA is:{self.complement()}")


class RNASequence(Sequence, Loggable, Serializable):
    def __init__(self, sequence):
        if not all(i in "AUGC" for i in sequence) and sequence != "":
            print("this isn't  a RNA sequence")
        super().__init__(sequence)

    def complement(self):
        structure = str.maketrans({"A": "U", "T": "A", "C": "G", "G": "C"})
        self.mRNA = self.sequence.translate(structure)
        return self.mRNA

    def present(self):
        print(
            f"the length of the dna sequence is:{self.length()}\n"
            f"the DNA sequence is:{self.sequence}\n"
            f"the complementary RNA of the sequence is:{self.complement()}"
        )


class ExperimentLogger:
    def __enter__(self):
        print("experience started")
        self.start = Decimal(str(time.time()))
        logging.info(f"the time of start was:{self.start.quantize(Decimal('0.01'))}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("experienced finished")
        self.end = Decimal(str(time.time()))
        self.duration = Decimal(str(self.end - self.start))
        logging.info(f"the time of duration was:{self.duration.quantize(Decimal('0.1'))}")
        return self


class DNALecture(Sequence):
    """Reads a DNA sequence three bases (one codon) at a time."""

    def __init__(self, sequence):
        super().__init__(sequence)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index + 3 > len(self.sequence):
            logging.error(f"there was error:{self.sequence[-2:]}")
            raise StopIteration
        self.codons = self.sequence[self.index: self.index + 3]
        self.index += 3
        return self.codons


def get_dna_input():
    while True:
        s = input("place a dna sequence:").upper()
        if all(i in "ATGC" for i in s) and s != "":
            return s
        print("this is not a dna sequence")


if __name__ == "__main__":
    s = get_dna_input()

    p = DNASequence(s)
    p.present()
    p.log(f"the DNA sequence {p.complement()} has been added")
    p.to_json()

    t = RNASequence(s)
    t.log(f"the RNA sequence {t.complement()} has been added")
    t.to_json()
    t.present()

    polymorph = [p, t]
    for poly in polymorph:
        print(poly.complement())
        print(type(poly).__name__)

    with ExperimentLogger() as exp:
        l_s = s * 10000
        s_o = DNASequence(l_s)
        s_t = RNASequence(l_s)
        for _ in range(5):
            s_o.complement()
            s_t.complement()
        print("the experience is done")
        with open("test.txt", "w", newline="", encoding="utf-8") as ts:
            test = {
                "length DNA": len(l_s),
                "DNA ": l_s,
                "mRNA": s_t.complement(),
                "cDNA": s_o.complement(),
            }
            json.dump(test, ts, indent=4)

    l_c = DNALecture(s)
    for codon in l_c:
        print(codon)
