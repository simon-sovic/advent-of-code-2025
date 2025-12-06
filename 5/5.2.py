
with open('input', 'r') as file:
    intervals = [ tuple(int(x) for x in line.split('-')) for line in file.read().split('\n\n')[0].split('\n') if len(line) > 0 ]


# Merge overlapping intervals
for idx2 in range(len(intervals) - 1, -1, -1):
    s2, e2 = intervals[idx2]
    for idx1 in range(idx2):
        s1, e1 = intervals[idx1]
        if s1 <= e2 and s2 <= e1:
            # intervals overlap
            intervals[idx1] = min(s1, s2), max(e1, e2)
            intervals.pop(idx2)
            break


fresh_count = 0
for s, e in intervals:
    fresh_count += e - s + 1

print(fresh_count)
