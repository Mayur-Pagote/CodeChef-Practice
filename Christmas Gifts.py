# cook your dish here

user_input = int(input())
for i in range(user_input):
    l = list(map(int, input().split()))
    print(500 // (l[0] * l[1] + l[1] * l[2] + l[2] * l[0] ))
