import math
a = int(input())

b = int(input())
l = int(input())
N = int(input())

q = (N // 2) - 1
D = a * math.sqrt(2)
print((D * N * 2) + l)    