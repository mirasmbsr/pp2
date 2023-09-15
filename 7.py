a = int(input())
b = int(input())
c = int(input())
if a // 2 != 0:
    a = a // 2 + 1
if b // 2 != 0:
    b = b // 2 + 1
if c // 2 != 0:
    c = c // 2 + 1
print(a + b + c)