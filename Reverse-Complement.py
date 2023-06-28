from DNA_Nucleotide_Counter import *

validatedSeq = userDNA.upper()
reverseComplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'} #Dictionary of complement nucleotides.

def dnaComplement(seq):
    return ''.join([reverseComplement[nuc] for nuc in seq])

print("The complementray to the positive strand is: ", dnaComplement(validatedSeq)) #Checkpoint - see if reverseComplement function actually works.

print()
print(f"DNA String + Complement: \n5'  {validatedSeq} 3' ")
print(f"    {''.join(['|' for c in range(len(validatedSeq))])}")
print(f"3'  {dnaComplement(validatedSeq)} 5'\n")

def dnaReverseComplement(seq):
    return ''.join([reverseComplement[nuc] for nuc in seq])[::-1]

print("The reverse complement to the validated sequence is: ", dnaReverseComplement(validatedSeq)) #produces a reverse complement to the user's input.
print()
