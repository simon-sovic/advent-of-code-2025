
with open('input', 'r') as file:
    intervals = [ tuple(int(x) for x in interval.split('-')) for interval in file.read().split(',') ]


invalid_id_sum = 0

for start, end in intervals:
    for id in range(start, end + 1):
        idstr = str(id)
        midx = len(idstr) // 2
        if idstr[:midx] == idstr[midx:]:
            invalid_id_sum += id

print(invalid_id_sum)
