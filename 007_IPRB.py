with open("data/rosalind_iprb.txt", "r") as input_file:
    k, m, n = map(int, input_file.read().rstrip().split(" "))

ans = 1 - (m * (m - 1)
       + 4 * m * n
       + 4 * n * (n - 1)) \
    / (4 * (k + m + n) * (k + m + n - 1))

ans = f"{ans:.5f}"
with open("output/007_IPRB.txt", "w") as output_file:
    output_file.write(ans)
    print(ans)
