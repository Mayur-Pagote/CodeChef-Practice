# cook your dish here
for i in range(int(input())):
    count=0
    x,y,z = map(int, input().split())
    count = max(count, x+y, y+z, x+z)
    print(count)
