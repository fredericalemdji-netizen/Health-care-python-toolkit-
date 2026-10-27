# Plasmodium falciparum Mitochondrial Genome Analysis

## Overview
This script performs numerical analysis of the *Plasmodium falciparum* mitochondrial genome (NCBI accession **AY282930.1**, 5,949 bases) using NumPy. It converts the raw DNA sequence into numerical representations and derives composition statistics, windowed GC content, and the reverse complement strand.

## Data Source
- Sequence: *Plasmodium falciparum* mitochondrial genome
- Accession: AY282930.1 (NCBI)
- Length: 5,949 bases

## What the script does
1. **Parsing** — reads the FASTA file, strips the header, and joins the sequence lines into one continuous string.
2. **Diagnostics & cleaning** — inspects the unique characters actually present in the raw sequence, then filters to keep only valid bases (A, C, G, T), discarding ambiguous or non-standard symbols.
3. **Integer encoding** — maps each base to an integer (A→0, C→1, G→2, T→3).
4. **One-hot encoding** — vectorized conversion of the integer-encoded sequence into a one-hot matrix using `np.eye`.
5. **Composition analysis**
   - Overall GC content and AT content across the full genome.
   - Windowed GC content (sequence split into equal-length windows) to see how composition varies along the genome, with summary statistics (mean, median, min, max) across windows.
6. **Reverse complement** — derives the reverse complementary DNA strand numerically (`3 - encoded`, reversed), plus the complementary (non-reversed) strand.
7. **Transcription** — produces the corresponding mRNA strand (T→U) from the reverse complement, and reshapes it into codon triplets.

## Requirements
- Python 3
- NumPy

## Usage
```bash
python real_biological_datasets_manipulation.py
