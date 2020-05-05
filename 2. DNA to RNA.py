# Author: Vasanth Desai
# Date: 04/05/2020
# Title: Convert DNA sequence to RNA

def dnaTorna(self):
    rna=self.replace('T','U')
    print(rna)

dnaSequence=input("Enter DNA Sequence : ").upper()

dnaTorna(dnaSequence)
