import string


a = '' # DAY 5 puzzle input snipped


pairs = set(zip(string.ascii_uppercase, string.ascii_lowercase) + zip(string.ascii_lowercase, string.ascii_uppercase))

def shrink_once(polymer):
    builder = ''
    current = 0
    shrunk = False
    while current < len(polymer):
        if (current + 1) >= len(polymer):
            builder += polymer[current]
            break
        if (polymer[current], polymer[current + 1]) in pairs:
            shrunk = True
            current += 2
        else:
            builder += polymer[current]
            current += 1
    return builder, shrunk

def shrink_all(polymer):
    builder, shrunk = shrink_once(polymer)
    while shrunk:
        builder, shrunk = shrink_once(builder)
    return builder

# Part 1
final_polymer = shrink_all(a)
print(len(final_polymer))

# Part 2
lengths = []
for letter in string.ascii_uppercase:
    test_polymer = a.replace(letter, '').replace(letter.lower(), '')
    lengths.append(len(shrink_all(test_polymer)))

print(min(lengths))