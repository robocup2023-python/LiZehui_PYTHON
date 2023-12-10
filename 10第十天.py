codon_amino = {
    "A": "GCG", "A": "GCA", "A": "GCC", "A": "GCU",
    "C": "UGC", "C": "UGU",
    "D": "GAC", "D": "GAU",
    "E": "GAG", "E": "GAA",
    "F": "UUC", "F": "UUU",
    "G": "GGG", "G": "GGA", "G": "GGC", "G": "GGU",
    "H": "CAC", "H": "CAU",
    "I": "AUA", "I": "AUC", "I": "AUU",
    "K": "AAG", "K": "AAA",
    "L": "UUG", "L": "UUA", "L": "CUG", "L": "CUA", "L": "CUC", "L": "CUU",
    "M": "AUG",
    "N": "AAC", "N": "AAU",
    "P": "CCG", "P": "CCA", "P": "CCC", "P": "CCU",
    "Q": "CAG", "Q": "CAA",
    "R": "CGG", "R": "CGA", "R": "CGC", "R": "CGU", "R": "AGG", "R": "AGA",
    "S": "UCG", "S": "UCA", "S": "UCC", "S": "UCU", "S": "AGC", "S": "AGU",
    "T": "ACG", "T": "ACA", "T": "ACC", "T": "ACU",
    "V": "GUA", "V": "GUG", "V": "GUU",
    "W": "UGG",
    "Y": "UAC", "Y": "UAU",
    "stop": "UAA", "stop": "UAG", "stop": "UGA"
}

sequence = "MSVAGTSSIDDPRPL"
amino_sequence = ""

for amino in sequence:
    codon = codon_amino[amino]
    if codon == "stop":
        break
    amino_sequence += codon

print(amino_sequence)
