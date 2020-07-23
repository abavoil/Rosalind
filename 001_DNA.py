with open("data/rosalind_dna.txt", "r") as input_file:
    dna = input_file.read().rstrip()

ans = " ".join([str(dna.count(nucleotide)) for nucleotide in "ACGT"])

with open("output/001_DNA.txt", "w") as output_file:
    output_file.write(ans)
    print(ans)
