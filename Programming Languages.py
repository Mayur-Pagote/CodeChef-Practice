# cook your dish here
for i in range(int(input())):
    count = 0
    a,b,a1,b1,a2,b2 = map(int, input().split())
    aset = [a1,b1]
    bset = [a2,b2]
    if a in aset and b in aset:
        count += 1
    elif a in bset and b in bset:
        count += 2
    
    print(count)
