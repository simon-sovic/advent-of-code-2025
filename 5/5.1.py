
with open('input', 'r') as file:
    file_parts = [ part for part in file.read().split('\n\n') if len(part) > 0 ]
    intervals = [ tuple(int(x) for x in line.split('-')) for line in file_parts[0].split('\n') if len(line) > 0 ]
    ids = [ int(line) for line in file_parts[1].split('\n') if len(line) > 0 ]
    del file_parts


fresh_count = 0
for id in ids:
    fresh_count += int(any( s <= id <= e for s, e in intervals ))

print(fresh_count)
