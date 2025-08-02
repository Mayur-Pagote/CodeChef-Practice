t = int(input())

while t > 0:
    x, y = map(int, input().split())
    # Your code goes here
    t -= 1
    if x >= y:
        print(y)
    else:
        res = y - x
        print((res*2)+x)
