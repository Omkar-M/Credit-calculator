from math import log
no1 = int(input())
no2 = int(input())
if no2 < 2:
    print(round(log(no1), 2))
else:
    print(round(log(no1, no2), 2))
