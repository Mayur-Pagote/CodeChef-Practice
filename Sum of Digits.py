# cook your dish here
user = int(input())

for i in range(user):
    num = int(input())
    count = 0
    while num > 0:
        res = num%10
        count += res
        num = num // 10
    print(count)
