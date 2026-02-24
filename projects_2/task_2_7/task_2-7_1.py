from datetime import datetime
import random

files = ["seq1", "seq2", "seq3", "seq4"]

now = str(datetime.now())

for name in files:

   new_name = name + ".fasta" + "\t" + now[:10] + " " + str(int(now[11:13]) - random.randint(0, 2)) + ":" + str(int(now[14:16]) - random.randint(0, 2)) + ":" + str(int(now[17:19]) - random.randint(0, 2))

   print(f"{new_name}")

