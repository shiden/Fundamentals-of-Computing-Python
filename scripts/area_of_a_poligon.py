import math

sides = 7
length = 3
top = sides * length ** 2
bottoma = math.pi/sides 
bottom = 4 * math.tan(bottoma)

solution = top / bottom
print solution
