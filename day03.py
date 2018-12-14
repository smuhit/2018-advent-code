a = [
    # DAY 3 puzzle input snipped
]


# PART 1
b = [[0 for i in range(1000)] for j in range(1000)]
shared = 0

for claim in a:
    parts = claim.split(' ')
    dimensions = parts[-1]
    coords = parts[-2].rstrip(':')
    x_start, y_start = coords.split(',')
    x_width, y_width = dimensions.split('x')
    x_end = int(x_start) + int(x_width)
    y_end = int(y_start) + int(y_width)
    for x in range(int(x_start), x_end):
        for y in range(int(y_start), y_end):
            if b[x][y] == 1:
                shared += 1
            b[x][y] += 1

print(shared)

# PART 2
b = [[set([]) for i in range(1000)] for j in range(1000)]
best_claim = set([])

for claim in a:
    parts = claim.split(' ')
    dimensions = parts[-1]
    coords = parts[-2].rstrip(':')
    claim_id = parts[0].lstrip('#')
    best_claim.add(claim_id)
    x_start, y_start = coords.split(',')
    x_width, y_width = dimensions.split('x')
    x_end = int(x_start) + int(x_width)
    y_end = int(y_start) + int(y_width)
    for x in range(int(x_start), x_end):
        for y in range(int(y_start), y_end):
            if b[x][y]:
                best_claim.discard(claim_id)
                for elem in b[x][y]:
                    best_claim.discard(elem)
            b[x][y].add(claim_id)

print(best_claim)
