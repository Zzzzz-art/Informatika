x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
AB = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
BC = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
AC = ((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5
P = AB + BC + AC
p = (AB + BC + AC) / 2
S = (p * (p - AB) * (p - BC) * (p - AC)) ** 0.5
print(P)
print(S)
