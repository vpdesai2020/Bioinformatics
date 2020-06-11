# Author: Vasanth Desai
# Date: 11/06/2020
# Title: Reading FASTA sequences from a file

def read_FASTA(file):
    with open(file) as fasta:
        return fasta.read().split('>')[1:]