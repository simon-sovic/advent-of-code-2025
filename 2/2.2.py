
with open('input', 'r') as file:
    intervals = [ tuple(int(x) for x in interval.split('-')) for interval in file.read().split(',') ]


invalid_id_sum = 0

for start, end in intervals:
    for id in range(start, end + 1):
        idstr = str(id)
        for n in range(1, len(idstr) // 2 + 1):
            if len(idstr) % n != 0:
                continue
            substr = idstr[:n]
            if all(idstr[i*n:(i+1)*n] == substr for i in range(1, len(idstr) // n)):
                invalid_id_sum += id
                break

print(invalid_id_sum)
