import math
a = int(input())
area_octahedron = round(2 * math.sqrt(3) * (a ** 2), 2)
vol_octahedron = round((1 / 3) * math.sqrt(2) * (a ** 3), 2)
print(f'{area_octahedron} {vol_octahedron}')
