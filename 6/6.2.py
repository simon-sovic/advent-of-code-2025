
with open('input', 'r') as file:
    lines = [ line for line in file.read().split('\n') if line.strip() != '' ]


operators = lines.pop().split()

indexes_of_separating_spaces = list(
    set(i for i, c in enumerate(lines[0])  if c == ' ') &
    set(i for i, c in enumerate(lines[-1]) if c == ' ')
)
indexes_of_separating_spaces.sort()

# Get the number substrings
ioss = indexes_of_separating_spaces
numbers = [ [ line[s+1:e] for s, e in zip([-1] + ioss, ioss + [None]) ] for line in lines ]

# Transpose the number matrix
numbers = list(map(list, zip(*numbers)))

# Transpose the characters in individual problems
numbers = [ list(map(lambda s: ''.join(s), zip(*nums))) for nums in numbers ]

# Evaluate the answer
answer = sum( eval(operator.join(nums)) for nums, operator in zip(numbers, operators) )

print(answer)
