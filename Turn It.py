# cook your dish here

import math
for i in range(int(input())):
    U,V,A,S = map(int, input().split())
    newton = U*U - (2*A*S)
    if newton <= 0:
        print("YES")
    elif newton**0.5 <= V:
        print("YES")
    else:
        print("NO")
