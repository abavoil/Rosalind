with open("data/rosalind_revc.txt", "r") as input_file:
    dna = input_file.read().rstrip()

ans = dna.translate(str.maketrans("ACGT", "TGCA"))[::-1]

with open("output/003_REVC.txt", "w") as output_file:
    output_file.write(ans)
    print(ans)
