t = int(input())

while t > 0:
    x, y, z = map(int, input().split())
    t -= 1
    res = (x*5) + (y*10)
    print(res//z)
