import pubchempy as pcp
import pandas as pd
from collections import deque

data = pd.read_csv("list_of_molecules.csv", header=None)

list_of_smiles = {}

for i in list_of_compounds:
    try:
        p=pcp.get_properties('IsomericSMILES','CC','smiles',searchtype='superstructure')
	list_of_smiles[i] = p
        print(p)
    except:
        print(i)
write.csv(list_of_smiles,"smiles.csv")




