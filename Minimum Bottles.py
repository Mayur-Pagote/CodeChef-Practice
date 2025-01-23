# cook your dish here
import math
T = int(input())

for i in range(T):
    N_X = list(map(int, input().split()))
    A = list(map(int, input().split()))
    print(math.ceil(sum(A) / N_X[1]))
