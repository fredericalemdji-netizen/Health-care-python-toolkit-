"""
Basic decorator example

A decorator that prints a line before and after the wrapped
function runs.

Extracted from exo_de_niveau_debutant__2_.py — the only live code
in that file; everything above it (including a second draft of the
Patient/PU classes) was commented out.
"""


def myDecorator(f):
    def wrapper(*args, **kwargs):
        print("runs before the input")
        r = f(*args, **kwargs)
        print("runs after the output")
        return r
    return wrapper


@myDecorator
def Say(name):
    print(f"hello {name}")


if __name__ == "__main__":
    Say("frederic")
