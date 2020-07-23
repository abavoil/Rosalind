with open("data/rosalind_rna.txt", "r") as input_file:
    dna = input_file.read().rstrip()

ans = dna.replace("T", "U")

with open("output/002_RNA.txt", "w") as output_file:
    output_file.write(ans)
    print(ans)
