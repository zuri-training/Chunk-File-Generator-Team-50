import pandas as pd
import os

file = "chunkfile/scripts/samplefile.csv"
rowSize = 100 # Number of records in each new file

def splitcsv():
    batchNumber = 1
    
    for chunk in pd.read_csv(file,chunksize=rowSize):
        chunk.to_csv(file + str(batchNumber) + ".csv", index=False)
        batchNumber += 1
        
splitcsv()