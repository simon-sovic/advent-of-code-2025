
with open('input', 'r') as file:
    lines = [ line for line in file.read().split('\n') if len(line) > 0 ]


output_joltage = 0
for line in lines:
    joltages = [ int(ch) for ch in line ]
    max_joltage = 0
    for i in range(len(joltages) - 1):
        first_joltage = joltages[i]
        a = first_joltage * 10
        if a < max_joltage:
            continue
        for j in range(i + 1, len(joltages)):
            second_joltage = joltages[j]
            joltage = a + second_joltage
            max_joltage = max(max_joltage, joltage)
    output_joltage += max_joltage

print(output_joltage)
