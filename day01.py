a = [
    # DAY 1 puzzle input snipped
]

# PART 1
total = 0

for x in a:
    total += x

print(total)


# PART 2
freq = 0
seen = set([freq])
found = False

while not found:
    for x in a:
        freq += x
        if freq in seen:
            found = True
            break
        seen.add(freq)

print(freq)
