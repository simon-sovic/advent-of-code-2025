
with open('input', 'r') as file:
    lines = [ line for line in file.read().split('\n') if len(line) > 0 ]



# Let's make the part 1 solution recursive!

_find_max_joltage_cache: dict[tuple[int, int], int] = dict()

def find_max_joltage(joltages: list[int], start_idx: int = 0, batteries_left: int = 12) -> int:

    if (start_idx, batteries_left) in _find_max_joltage_cache:
        return _find_max_joltage_cache[(start_idx, batteries_left)]

    if batteries_left == 0:
        return 0

    max_joltage = 0
    for idx in range(start_idx, len(joltages) - batteries_left + 1):
        joltage = joltages[idx] * 10 ** (batteries_left - 1)

        for next_idx in range(idx + 1, len(joltages) - batteries_left + 2):
            max_joltage = max(
                max_joltage,
                joltage + find_max_joltage(joltages, next_idx, batteries_left - 1)
            )

    _find_max_joltage_cache[(start_idx, batteries_left)] = max_joltage 
    return max_joltage


output_joltage = 0
for line in lines:
    joltages = [ int(ch) for ch in line ]
    output_joltage += find_max_joltage(joltages)
    _find_max_joltage_cache.clear()

print(output_joltage)
