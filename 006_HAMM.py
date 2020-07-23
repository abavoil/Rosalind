with open("data/rosalind_hamm.txt", "r") as input_file:
    s, t = input_file.read().rstrip().split()

hamming_distance = sum(s[i] != t[i] for i in range(len(s)))

ans = str(hamming_distance)
with open("output/006_HAMM.txt", "w") as output_file:
    output_file.write(ans)
    print(ans)
