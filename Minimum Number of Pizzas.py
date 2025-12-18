import math

for i in range(int(input())):
    friends, slize = map(int, input().split())
    count = friends // math.gcd(friends, slize)
    print(count)
