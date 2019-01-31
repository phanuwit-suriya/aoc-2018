import numpy as np


def power(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = str(power_level)
    return int(power_level[-3]) - 5 if len(power_level) > 2 else 0


serial_number = 7803
grid = np.full((301, 301), fill_value=0, dtype=np.int64, order='F')

for i in range(1,301):
    for j in range(1,301):
        grid[i][j] = power(i, j, serial_number)

total_power = 0
for k in range(3, 301):
    for j in range(1, 301-k):
        for i in range(1, 301-k):
            if np.sum(grid[i:i+k, j:j+k].transpose()) > total_power:
                total_power = np.sum(grid[i:i+k, j:j+k].transpose())
                x, y, size = i, j, k
    if k == 3:
        print(x, y, total_power)

print(x, y, size, total_power)