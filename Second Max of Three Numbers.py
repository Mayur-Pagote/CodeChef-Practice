# cook your dish here

user = int(input())

for i in range(user):
    x, y, z = map(int, input().split())

    if (x > y and x < z) or (x < y and x > z):
        print(x)
    elif (y > x and y < z) or (y < x and y > z):
        print(y)
    else:
        print(z)
