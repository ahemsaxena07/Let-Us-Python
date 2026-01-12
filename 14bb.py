#hanai problem
def hanai(n, source, destination, auxilary):
    if n == 1:
        print(f"move disk from {source} to {auxilary}")
        return
    hanai(n-1, source, destination, auxilary)
    print(f"move disk from {source} to {auxilary}")
    hanai(n-1, auxilary, destination, source)
print(hanai(4, "A", "B", "C"))