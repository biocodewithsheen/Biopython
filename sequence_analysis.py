import Bio
from Bio.Seq import Seq
dna_=("ATGGCAGCATG")
dna=Seq(dna_)

print(dna.complement())
      #complementary DNA

print("rna:",dna.transcribe())
       #mRNA 

print("protein:",dna.translate())
        #protein translated 


