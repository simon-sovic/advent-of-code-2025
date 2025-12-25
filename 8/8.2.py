
with open('input', 'r') as file:
    positions = [ tuple(int(x) for x in line.split(',')) for line in file.read().split('\n') if line.strip() != '' ]


type pos = tuple[int, int, int]

circuits: list[set[pos]] = [ {p} for p in positions ]


def update_circuits(connected_pos_1: pos, connected_pos_2: pos):
    circuit_1 = next( c for c in circuits if connected_pos_1 in c )
    circuit_2 = next( c for c in circuits if connected_pos_2 in c )

    if circuit_1 is circuit_2:
        # Both positions are already in the same circuit
        return
    # Else, merge the two circuits
    circuit_1 |= circuit_2
    circuits.remove(circuit_2)


def dist_sq(pos1: pos, pos2: pos) -> int:
    return sum( d**2 for d in ( abs(co1 - co2) for co1, co2 in zip(pos1, pos2) ) )


# For each pair of positions, find the distances between them
distances: list[tuple[int, pos, pos]] = []
for i1, pos1 in enumerate(positions):
    for pos2 in positions[i1+1:]:
        distances.append( (dist_sq(pos1, pos2), pos1, pos2) )


# Sort distances
distances.sort(key=lambda x: x[0])


# Keep connecting the closest pairs until there is only 1 circuit
for _, pos1, pos2 in distances:
    update_circuits(pos1, pos2)
    if len(circuits) == 1:
        break


answer = pos1[0] * pos2[0]
print(answer)
