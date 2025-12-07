
with open('input', 'r') as file:
    lines: list[str] = [ line for line in file.read().split('\n') if line.strip() != '' ]

idxs_of_beams: set[int] = { lines[0].find('S') }

rows_of_splitters: list[set[int]] = [ { i for i, c in enumerate(line) if c == '^' } for line in lines if line.find('^') != -1 ]

# Simulate the beams
split_count = 0
for idxs_of_splitters in rows_of_splitters:
    new_idxs_of_beams: set[int] = set()
    for idx_of_beam in idxs_of_beams:
        if idx_of_beam not in idxs_of_splitters:
            new_idxs_of_beams.add(idx_of_beam)
        else:
            new_idxs_of_beams.add(idx_of_beam - 1)
            new_idxs_of_beams.add(idx_of_beam + 1)
            split_count += 1
    idxs_of_beams = new_idxs_of_beams

print(split_count)
