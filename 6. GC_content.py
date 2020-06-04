# Author: Vasanth Desai
# Date: 04/06/2020
# Title: compute the GC content of a DNA sequence

def gc_content (dna_seq):
    gc_count = 0 
    for s in dna_seq:
        if s in "GCgc": gc_count += 1 
    return gc_count / len(dna_seq)
