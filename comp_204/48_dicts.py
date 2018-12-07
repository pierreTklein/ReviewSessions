sequence = "ACGGTGGT"
sequenceLength = 3
frequencies = {}
for i in range(len(sequence) - sequenceLength + 1):
    snippet = sequence[i:i + sequenceLength]
    if snippet not in frequencies:
        frequencies[snippet] = 0
    frequencies[snippet] += 1
print(frequencies)
