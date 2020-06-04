def reverse_complement (dna_seq):
    assert validate_dna(dna_seq), "Invalid DNA sequence" 
    comp = "" 
    for c in dna_seq.upper(): 
        if c ==’A’:
            comp = "T" + comp
        elif c =="T":
            comp = "A" + comp
        elif c =="G":
            comp = "C" + comp
        elif c== "C":
            comp = "G" + comp
    return comp