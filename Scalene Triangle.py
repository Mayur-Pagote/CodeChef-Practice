t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    # Your code goes here
    t -= 1
    if a!=b and b!=c and a!=c:
        print("YES")
    else:
        print("NO")
