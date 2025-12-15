# cook your dish here
for i in range(int(input())):
    a,b,c,d,K = map(int, input().split())
    
    distance = abs(a-c) + abs(b-d)
    
    if distance <= K and (K-distance) % 2 == 0:
        print("YES")
    else:
        print("NO")
