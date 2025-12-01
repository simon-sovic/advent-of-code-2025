


with open('input', 'r') as file:
    lines = [ line for line in file.read().split('\n') if len(line) > 0 ]

pos = 50
count = 0

for line in lines:
    val = int(line[1:])
    val *= { 'L': -1, 'R': 1 }[line[0]]
    pos += val
    pos %= 100
    count += int(pos == 0)

print(count)
