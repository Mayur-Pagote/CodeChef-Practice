# cook your dish here
user = int(input())

for i in range(user):
    x = int(input())
    s = input()
    Carlsen = 0
    Chef = 0
    for i in s:
        if i == "C":
            Carlsen += 2
        elif i == "N":
            Chef += 2
        elif i == "D":
            Chef += 1
            Carlsen += 1
    
    if Carlsen == Chef:
        print(55 * x)
    elif Carlsen > Chef:
        print(60 * x)
    else:
        print(40 * x)
        
