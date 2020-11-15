import math
a = float(input())
b = float(input())
ugol = float(input())
alpha = ugol*math.pi/180
print((a**2-b**2)/4*math.tan(alpha))
