def parseFASTA(data):
    # split data around ">" to seperates entries
    data = data.split(">")[1:]
    # then split each entry around "\n" to seperate its label from the strings
    data = [entry.split("\n", 1) for entry in data]
    # finally remove "\n" between DNA strings
    data = [[label, "".join(strings.split("\n"))] for label, strings in data]
    return data

if __name__ == '__main__':
    data = """>Rosalind_1769
TCGGCACGGAGTTCTATAGCCCTATCAGTACCACGCCTGTAACCAAGACATCGTCCGAAG
TCGGCACGGAGTTCTATAGCCCTATCAGTACCACGCCTGTAACCAAGACATCGTCCGAAG
>Rosalind_9598
TTAATCGCCGTCCAACTTTTTGTCTTTAAGATGCTGCGGAAACGGCCATGGTGTCGTAGA
TTAATCGCCGTCCAACTTTTTGTCTTTAAGATGCTGCGGAAACGGCCATGGTGTCGTAGA
>Rosalind_7652
CAGGCCATTAGGAGCGCACCCCACGCCGATTTGAATGATAGTCTATAGTAACCGTTACGG
CAGGCCATTAGGAGCGCACCCCACGCCGATTTGAATGATAGTCTATAGTAACCGTTACGG"""
    fasta = parseFASTA(data)
    print(*fasta, sep="\n")
