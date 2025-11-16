# cook your dish here
for i in range(int(input())):
    x, y, z, j, k = map(int, input().split())
    weight = y - x          # w2 - w1
    if (z * k) <= weight <= (j * k):   # x1*M  and  x2*M
        print(1)
    else:
        print(0)
