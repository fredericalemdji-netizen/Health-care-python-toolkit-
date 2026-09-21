"""
Sample tracking with UUID-based IDs (EXO 32)

Generates a unique ID per sample (a running counter plus a short
UUID4 fragment) and appends each sample record to a JSONL log.

Extracted from exercise_of_level_intermediare.py.
"""

import datetime as dt
import json
import logging
import uuid

logging.basicConfig(filename="min.log", level=logging.INFO)


class Sample:
    _counter = 0

    def __init__(self):
        Sample._counter += 1
        generated_id = f"SAMPLE - {Sample._counter:04d}-{uuid.uuid4().hex[:4]}"
        self.record = generated_id

    def Save(self):
        recording = json.dumps(vars(self), default=str) + "\n"
        with open("sample_log.jsonl", "a", newline="", encoding="utf-8") as t:
            t.write(recording + "\n")
        return logging.info("the sample %s was save on the %s", vars(self), dt.datetime.now())


class BloodSample(Sample):
    def __init__(self, glucose_level):
        super().__init__()
        self.glucose_level = glucose_level


class TissueSample(Sample):
    def __init__(self, cell_count):
        super().__init__()
        self.cell_count = cell_count


if __name__ == "__main__":
    g = input("place the glucose level of the bloodsample:")
    c = input("place the number of cells analyse:")
    S = Sample()
    B = BloodSample(g)
    C = TissueSample(c)
    print(Sample.__mro__, BloodSample.__mro__, TissueSample.__mro__)
    S.Save()
    B.Save()
    C.Save()
