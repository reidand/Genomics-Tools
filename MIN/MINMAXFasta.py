# This tool will return the maximum and minimum sequence length in a fasta file
f = open("dna2.fasta", "r")
file = f.readlines()

sequences = []
seq = ""
for f in file:
    if not f.startswith('>'):
        f = f.replace(" ", "")
        f = f.replace("\n", "")
        seq = seq + f
    else:
        sequences.append(seq)
        seq = ""

# Add the last seq
sequences.append(seq)

sequences = sequences[1:]

lengths = [len(i) for i in sequences]

print(max(lengths), min(lengths))
