t = int(input())
for _ in range(t):
    N, S = map(int, input().split())
    print(min(S, 2*N - S))
