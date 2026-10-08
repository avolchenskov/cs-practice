import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
sp = read_valid(lines)
average_temp = average_by_city(sp)
warm_city = warmest_city(sp)
print(len(sp), len(lines) - len(sp), f'{average_temp[warm_city]:.1f}', sep='\n')
