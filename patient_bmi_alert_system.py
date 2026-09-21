"""
Patient BMI & tension alert system (EXO 28-31)

A Patient base class, extended by PU with arterial/ventricular
tension and an alert level. Each record is appended to a JSONL file.

Extracted from exo_de_niveau_debutant.py — the only live code in that
file; everything else there was earlier commented-out drafts.
Cleanup made here: moved `import json` to the top of the file
(originally imported inside save()).
"""

import json


class Patient:
    def __init__(self, name, age, disease, height, weight):
        self.name = name
        self.age = age
        self.disease = disease
        self.height = height
        self.weight = weight

    def BMI(self):
        return round(self.weight / (self.height ** 2), 2)

    def status(self):
        bmi = self.BMI()
        if bmi > 24:
            return "overweight try to reduce, alert level 2"
        elif bmi < 24:
            return "underweight try to eat more but moderately, alert level 1"
        else:
            return "your are in good health, ok no alert but be careful"


class PU(Patient):
    def __init__(self, name, age, disease, height, weight, art_tens, ven_tens):
        super().__init__(name, age, disease, height, weight)
        self.art_tens = art_tens
        self.ven_tens = ven_tens

    def avr_tens(self):
        return round((self.art_tens + self.ven_tens) / 2, 2)

    def Alert(self):
        alert_tens = self.avr_tens()
        if alert_tens >= 140 or self.BMI() >= 25:
            return "go to the hospital"
        elif alert_tens <= 135 or self.BMI() <= 18.5:
            return "still go to the hospital"
        else:
            return "you can stay home"

    def present(self):
        print(
            f"patient name: {self.name} | patient age: {self.age}years | "
            f"patient height: {self.height}cm | patient weight: {self.weight}kg"
            f"| sickness: {self.disease}| Status of patient BMI: {self.status()}"
            f"| BMI of patient: {self.BMI()} | level of alert of patient: {self.Alert()}"
            f"| average tension of the patient: {self.avr_tens()}"
            f"| arterial tension of patient : {self.art_tens}) | ventricular tension: {self.ven_tens}"
        )

    def save(self):
        with open("data_of_test.jsonl", "a", newline="", encoding="utf-8") as f:
            rec = json.dumps(vars(self), default=str) + "\n"
            f.write(rec + "\n")


if __name__ == "__main__":
    patient_number = 1
    while patient_number <= 2:
        n = input("your name please:").strip()
        a = int(input("your age please:"))
        d = input("Your illness please be sincere:").strip()
        h = float(input("your height please:"))
        w = float(input("your weight and don't be ashame:"))
        a_t = float(input("place the aterial tension:"))
        v_t = int(input("place the venticular tension:"))
        p = PU(n, a, d, h, w, a_t, v_t)
        p.present()
        p.save()
        patient_number += 1
