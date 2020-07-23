from rosalib.FASTA import parseFASTA

with open("data/rosalind_gc.txt", "r") as input_file:
    data = parseFASTA(input_file.read())

for label, dna in data:
    gc_content = (dna.count("G") + dna.count("C")) / len(dna)

    try:
        if gc_content > best_gc_content:
            best_label, best_gc_content = label, gc_content
    except NameError:
        best_label, best_gc_content = label, gc_content

ans = f"{best_label}\n{100*best_gc_content:.6f}"
with open("output/005_GC.txt", "w") as output_file:
    output_file.write(ans)
    print(ans)
