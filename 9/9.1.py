
with open('input', 'r') as file:
    positions = [ tuple(int(x) for x in line.split(',')) for line in file.readlines() if line.strip() ]

max_area = 0
for i1, (x1, y1) in enumerate(positions):
    for x2, y2 in positions[i1+1:]:
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        max_area = max(max_area, area)

print(max_area)
