"""
DNA sequence validated via property getter/setter/deleter (EXO 6)

Extracted from exercise__early_advance_apply_to_bio.py.

Bug fixed from the original: the last line printed `D.__sequence`
directly, which fails outside the class because of name mangling
(Python rewrites `__sequence` to `_DNA_Sequence__sequence`). Access
it through the public `sequence` property instead.
"""


class InvalidSequenceError(Exception):
    pass


class DNA_Sequence:
    def __init__(self):
        self.__sequence = None

    @property
    def sequence(self):
        print("the getter is called to get a value")
        return self.__sequence

    @sequence.setter
    def sequence(self, val):
        self.__sequence = val
        print("the setter is set to a correct value")
        if not all(i in "ATGC" for i in val) or val == "":
            raise InvalidSequenceError(f"the sequence {val} was invalid")
        print("the value is set")

    @sequence.deleter
    def sequence(self):
        print("the value is being deleted")
        del self.__sequence
        print("the value is deleted")


if __name__ == "__main__":
    D = DNA_Sequence()
    D.sequence = input("place a setter value:").strip().upper()
    print(f"the setter value is {D.sequence}")
