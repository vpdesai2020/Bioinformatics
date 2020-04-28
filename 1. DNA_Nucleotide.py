# Author: Vasanth Desai
# Date: 28/04/2020
# Title: Counting DNA Nucleotides and GC content

#dnaSequence = "atcgatgagagctagcgata"
def dnaSequenceCount(self):
    aCount = 0
    cCount = 0
    tCount = 0
    gCount = 0
    allowed_bases = ["a", "t", "g", "c"]
    total_dna_bases = 0

    for c in dnaSequence:
        if c == 'a':
            aCount = aCount + 1
        elif c == 'c':
            cCount = cCount + 1
        elif c == 't':
            tCount = tCount + 1
        elif c == 'g':
            gCount = gCount + 1

    sequenceLength = len(self)
    for base in allowed_bases:
        total_dna_bases = total_dna_bases + self.count(base)

    

    print("Total DNA bases: %d \n"%total_dna_bases)
    print ("Percentage of Adenine (A's) in sequence:", (float(aCount) / sequenceLength) * 100)
    print ("Percentage of Cytosine (C's) in sequence:", (float(cCount) / sequenceLength) * 100)
    print ("Percentage of Thymine (T's) in sequence:", (float(tCount) / sequenceLength) * 100)
    print ("Percentage of Guanine (G's) in sequence:", (float(gCount) / sequenceLength) * 100,"\n")
    print("GC Content :", (float(gCount+cCount)*100.0)/total_dna_bases)


dnaSequence=input("Enter DNA Sequence : ").lower()

dnaSequenceCount(dnaSequence)
