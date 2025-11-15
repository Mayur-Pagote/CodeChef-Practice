# cook your dish here
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    if K == 0:
        print(N)
    else:
        print(N % K)
