"""
Dose validation generator

Collects a few raw dose inputs, then yields only the ones that
convert cleanly to a positive Decimal, skipping anything invalid.

Extracted from exercise_of_level_intermediare.py — a standalone
exercise, unrelated to the DNA/RNA classes elsewhere in that file.
"""

from decimal import Decimal, InvalidOperation

doses = []


def filter_valide_doses():
    count = 3
    while count > 0:
        dose = input("place a dose:")
        count -= 1
        doses.append(dose)
    for d in doses:
        try:
            value = Decimal(d)
            if value > 0:
                yield value
        except InvalidOperation:
            pass


if __name__ == "__main__":
    for valid_dose in filter_valide_doses():
        print(valid_dose)
    print(doses)
