import numpy as np

# 1. Read the real FASTA file
with open("AY282930.1.fna.txt", "r", encoding="utf-8") as f:
    next(f)  # skip header
    seq = "".join(i.strip() for i in f)

print(len(seq))

# 2. Diagnosing — convert to array and check what's actually present
seq_arr = np.array(list(seq))
diag, counts = np.unique(seq_arr, return_counts=True)
print(diag)
print(counts)

# 3. Cleaning — keep only real bases, not whatever diag happens to contain
valid_bases = np.array(["A", "C", "G", "T"])
mask = np.isin(seq_arr, valid_bases)
clean_seq = seq_arr[mask]
print(clean_seq.shape[0])

# 4. Integer encoding
bases = {"A": 0, "C": 1, "G": 2, "T": 3}
encoded = np.array([bases[b] for b in clean_seq])
print(encoded[:10])

# 5. One-hot encoding, vectorized, no loop
enc_seq = np.eye(4)[encoded]
print(enc_seq, enc_seq.shape)

#6 calculating the GC and AT content
is_gc = (encoded == 1) | (encoded == 2)
res = is_gc.reshape(-1, 661)
is_at = (encoded == 0) | (encoded == 3)
GC_content = (np.sum(is_gc)/encoded.size)*100
res_sum = (np.sum(res, axis = 1)/ res.shape[1])*100
print(res_sum, np.mean(res_sum))

AT_content = (np.sum(is_at)/encoded.size)*100


print(f"the GC content of the DNA mitochondrion of falciparium plasmodium is {GC_content}%, the AT content of the DNA mitochondrion of plasmodium falciparium is {AT_content}%")

#7 bringing out the reverse complementary strand of the DNA of the motochondrion of plasmodium falciparium


rev_cDNA = (3 - encoded)[::-1]
print("the reverse complementary DNA is", rev_cDNA[:10])
cdna = 3 - encoded
print("the DNA is", encoded[:10])
print(encoded[-10:])


rna_let = np.array(["A", "C", "G", "U" ])
RNA = rna_let[rev_cDNA]
DNA = valid_bases[encoded]
cDNA = valid_bases[cdna]


print("the DNA strand", DNA[:10])
print("the complementary DNA strand", cDNA[:10])
print("the mRNA strand", RNA[:10])
print(valid_bases[np.argmax(enc_seq, axis = 1)])


test = RNA[:].reshape(-1, 3)
print(test)
print(test.shape)

#calculating the mean of the number of nucleotides in other word 
mean = np.mean(enc_seq, axis = 0)
print(mean*100, "%", mean.shape)
sort = np.sort(res_sum)
print(
f"the sorted values  = {sort}\n"
f"the median value is {np.median(res_sum)}\n"
f"the min and max values respectively {np.min(res_sum)} & {np.max(res_sum)}")
