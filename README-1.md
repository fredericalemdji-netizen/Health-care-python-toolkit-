# Healthcare Python Toolkit

**A self-directed healthtech software project.**

An independent set of Python tools built from the ground up while studying Biomedical Engineering, aimed at real, documented problems facing healthcare delivery in Cameroon: workforce shortages, fragmented patient records, and facilities that need software to work offline-first. This repository holds the working code produced along that path — patient data systems, DNA/RNA sequence tools, and data-cleaning pipelines — each script standalone, tested, and runnable on its own.

## Why this exists

Cameroon has roughly 0.8 doctors per 10,000 people, well below WHO-recommended levels, and healthcare delivery is widely documented as constrained by fragmented, disconnected information systems between providers and facilities. This is a long-term effort to build software that addresses that directly — starting with the fundamentals, and building toward a pilot-ready product.

## What's in this repository

| File | Description |
|---|---|
| `patient_bmi_alert_system.py` | Patient/PU class hierarchy computing BMI, tension averages, and a hospital-visit alert level; saves records to JSONL |
| `dna_rna_sequence_oop.py` | Mixin-based OOP pipeline for DNA/RNA sequences — complement calculation, timed experiment runs via a context manager, and a codon-reading iterator |
| `dna_sequence_property_validator.py` | A DNA sequence class validated through a property getter/setter/deleter |
| `sample_uuid_tracking.py` | Lab sample tracking with unique, generated IDs (blood and tissue sample subclasses) |
| `patient_dataclass_property_demo.py` | A `@dataclass`-based Patient model with age validated through a property |
| `dose_validation_generator.py` | A generator that filters raw dose input down to valid, positive values |
| `decorator_basic_example.py` | A basic before/after logging decorator |

## Tech stack

- **Python 3.13**
- **NumPy**, **pandas**, **openpyxl** — data handling and export
- **Biopython** (installed, upcoming) — sequence and structural biology work
- Standard library: `csv`, `json`, `logging`, `datetime`, `decimal`, `uuid`

## Roadmap

This repository reflects an active, in-progress curriculum, not a finished product:

- [x] Python OOP fundamentals — classes, inheritance, decorators, context managers, iterators/generators
- [x] NumPy Level 1–2 — array foundations, vectorization
- [ ] NumPy Level 3–8 — matrix math, broadcasting, biological data representation, statistics, simulation, performance
- [ ] pandas — cleaning, grouping, merging, time series
- [ ] Biopython — sequence parsing, alignment, structural biology (`Bio.PDB`)
- [ ] SciPy — statistics, signal processing, optimization
- [ ] Pilot-ready patient system, targeting local district hospitals and clinics

## License

Released under the [MIT License](LICENSE).
