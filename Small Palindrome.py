# cook your dish here
user = int(input())
s = ""
for i in range(user):
    a,b = map(int, input().split())
    a_freq = a//2
    s = ("1" *a_freq) + ("2" * b) + ("1" *a_freq)
    print(int(s))
