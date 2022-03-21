from math import gcd
from itertools import combinations

for t in range(int(input())):print(max([gcd(x, y) for x,y in combinations(map(int, input().split()), 2)]))