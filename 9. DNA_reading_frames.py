# Author: Vasanth Desai
# Date: 06/06/2020
# Title: Computes the six reading frames of a DNA sequence (including the reverse complement)

def reading_frames (dna_seq):
    assert validate_dna(dna_seq), "Invalid DNA sequence" #from previous 'validate_dna' code
    res = []
    res.append(translate_seq(dna_seq,0))
    res.append(translate_seq(dna_seq,1))
    res.append(translate_seq(dna_seq,2))
    rc = reverse_complement(dna_seq)
    res.append(translate_seq(rc,0))
    res.append(translate_seq(rc,1))
    res.append(translate_seq(rc,2))
    return res