
with open('input', 'r') as file:
    lines: list[str] = [ line for line in file.read().split('\n') if line.strip() != '' ]

grid_cols = len(lines[0])

counts_of_particles_at_idxs: list[int] = [0] * grid_cols
counts_of_particles_at_idxs[lines[0].find('S')] = 1

rows_of_splitters: list[set[int]] = [ { i for i, c in enumerate(line) if c == '^' } for line in lines if line.find('^') != -1 ]

# Simulate the particles
for idxs_of_splitters in rows_of_splitters:
    new_counts_of_particles_at_idxs: list[int] = [0] * grid_cols
    for idxs_of_particles, count_of_particles in enumerate(counts_of_particles_at_idxs):
        if count_of_particles == 0:
            continue
        if idxs_of_particles not in idxs_of_splitters:
            new_counts_of_particles_at_idxs[idxs_of_particles] += count_of_particles
        else:
            new_counts_of_particles_at_idxs[idxs_of_particles - 1] += count_of_particles
            new_counts_of_particles_at_idxs[idxs_of_particles + 1] += count_of_particles
    counts_of_particles_at_idxs = new_counts_of_particles_at_idxs

# Count the particles
timeline_count = sum(counts_of_particles_at_idxs)
print(timeline_count)
