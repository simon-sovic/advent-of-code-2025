


with open('input', 'r') as file:
    lines = [ line for line in file.read().split('\n') if len(line) > 0 ]

pos = 50
count = 0

for line in lines:
    val = int(line[1:])

    # Handle cases where abs(val) > 99
    extra_rotations = val // 100
    count += extra_rotations
    val -= extra_rotations * 100

    sign *= { 'L': -1, 'R': 1 }[line[0]]

    ppos = 100 if sign < 0 and pos == 0 else pos
    pos += val * sign
    pos %= 100

    count += int(sign > 0 and ppos > pos or sign < 0 and (ppos < pos or pos == 0))

print(count)
