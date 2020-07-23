with open("data/rosalind_fib.txt", "r") as input_file:
    n, k = map(int, input_file.read().rstrip().split())

a, b = 0, 1
for month in range(n - 1):
    a, b = b, k * a + b
ans = str(b)

with open("output/004_FIB.txt", "w") as output_file:
    output_file.write(ans)
    print(ans)
