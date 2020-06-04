# Author: Vasanth Desai
# Date: 04/06/2020
# Title:Translates a DNA sequence into an aminoacid sequence

def translate_seq (dna_seq, ini_pos = 0):
    assert validate_dna(dna_seq), "Invalid DNA sequence" 
    seqm = dna_seq.upper() 
    seq_aa = "" 
    for pos in range(ini_pos,len(seqm)−2,3): 
        cod = seqm[pos:pos+3] 
        seq_aa += translate_codon(cod) #Using the previous function 4. codon_to_aminoacid
    return seq_aa
