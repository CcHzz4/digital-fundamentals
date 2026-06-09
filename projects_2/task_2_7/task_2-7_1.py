files = ["seq1", "seq2", "seq3", "seq4"]
date = "2004-04-20"

for name in files:
    new_name = name + "_" + date + ".fasta"
    print(new_name)
