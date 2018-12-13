from collections import Counter

a = [
    # DAY 2 Puzzle input snipped
]

twines = 0
thrines = 0

for x in a:
    y = Counter(x)
    has_twine = False
    has_thrine = False
    for z in y.most_common():
        if z[1] == 2:
            has_twine = True
        if z[1] == 3:
            has_thrine = True
        if z[1] < 2:
            break
    if has_twine:
        twines += 1
    if has_thrine:
        thrines += 1

print(twines * thrines)

sorted_a = sorted(a)
len_id = len(sorted_a[0])
mostest = None

for x in range(len_id):
	tester = [z[:x] + z[x+1:] for z in sorted_a]
	y = Counter(tester)
	w = y.most_common(1)
	if w[0][1] > 1:
		mostest = w[0][0]
		break

print(mostest)
