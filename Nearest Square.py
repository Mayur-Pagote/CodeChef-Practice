import math

# Read number of test cases
user = int(input())

for _ in range(user):
    x = int(input())
    # Find the largest integer whose square is less than or equal to x
    count = int(math.sqrt(x))
    print(count * count)
