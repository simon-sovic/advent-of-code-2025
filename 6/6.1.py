
with open('input', 'r') as file:
    tokens = [ line.split() for line in file.read().split('\n') if line.strip() != '' ]


operators = tokens.pop()    # separate the operators from the numbers
numbers = list(map(list, zip(*tokens))) # transpose the remaining matrix of numbers so that
                                        # each problem's numbers are in their own line

answer = sum( eval(operator.join(nums)) for nums, operator in zip(numbers, operators) )
print(answer)
