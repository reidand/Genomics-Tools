# Tool to return the number of records in a FASTA file

f=open("FILENAME.fasta","r")
file = f.read()
print(file.count('>'))
