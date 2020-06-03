# Author: Vasanth Desai
# Date: 03/06/2020
# Title: Checks if DNA sequence is valid
def validating_DNA (dna_seq):
    seqm = dna_seq.upper()
    valid = seqm.count("A") + seqm.count("C") + seqm.count("G")+ seqm.count("T")
    if valid == len(seqm): 
        
        return True 
        
    else: 
       
        return False
validating_DNA("atgxattgc") #input sequence