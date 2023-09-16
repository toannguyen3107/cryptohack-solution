
import math
def solve(n):
    sq_root = int(math.sqrt(n))
    return (sq_root * sq_root) == n
for i in range(0, 1111):
    x = 14+29*i
    y = 6+29*i
    z = 11+29*i
    if solve(x) == True:
        print(x)
        break
    elif solve(y) == True:
        print(y)
        break
    elif solve(z) ==True:
        print(z)
        break


