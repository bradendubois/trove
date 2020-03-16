from sys import stdin
from random import randint

for line in stdin:

    if "+" not in line:
        continue

    values = [x.strip() for x in line.rstrip().split("+")]
    total = 0

    for value in values:

        if not value.isdigit():
            continue

        if randint(0, 1):
            total += int(value)
        else:
            total = int(str(total) + value)

    print(total)
