# cook your dish here

user_input = int(input())

for i in range(user_input):
    a,b = map(int, input().split())
    sp_inp = input()
    count = sp_inp.count("S")
    res = b - count
    if res > 0 :
        f_res = res + a - 1
    else:
        f_res = a
    print(f_res)
