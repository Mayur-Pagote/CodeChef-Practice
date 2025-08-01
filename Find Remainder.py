# cook your dish here
user = int(input())

for i in range(user):
    a,b = map(int, input().split())
    print(a%b)
