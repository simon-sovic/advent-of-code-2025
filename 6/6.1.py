
with open('input', 'r') as file:
    tokens = [ line.split() for line in file.read().split('\n') if line.strip() != '' ]

# Separate the operators from the numbers
operators = tokens.pop()

# Transpose the remaining matrix of numbers so that
#  each problem's numbers are in their own line
numbers = list(map(list, zip(*tokens)))

answer = sum( eval(operator.join(nums)) for nums, operator in zip(numbers, operators) )
print(answer)
