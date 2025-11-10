# cook your dish here
for i in range(int(input())):
    x,y = map(int, input().split())
    count = 0
    for j in range(x):
        k, l = map(int, input().split())
        if k <= y:
            count = max(count,l)
    print(count)
