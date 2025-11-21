for _ in range(int(input())):
    N = int(input())
    if N % 4 == 1 or N % 4 == 2:
        print(N - 1)
    else:
        print(N)
