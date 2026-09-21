"""
Dataclass + property demo (EXO 21)

A Patient dataclass whose age is validated through a property
setter rather than being accepted as-is.

Extracted from exercise_of_level_intermediare.py.
"""

from dataclasses import dataclass, field


@dataclass
class Patient:
    name: str
    age: int = 0
    dose: list = field(default_factory=list)

    @property
    def age(self):
        print("getter was called")
        return self._age

    @age.setter
    def age(self, val):
        print("setter was called,", val)
        if val < 0 or val > 100:
            raise ValueError("the age was not making sense")
        self._age = val


if __name__ == "__main__":
    n = str(input("place a name:"))
    a = int(input("place an age:"))
    p = Patient(n, a)
    p.age = 50
    print(p.age)
