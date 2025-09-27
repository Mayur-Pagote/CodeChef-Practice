# cook your dish here
for i in range(int(input())):
    user = int(input())
    if user < 3:
        print("LIGHT")
    elif user >= 3 and user < 7:
        print("MODERATE")
    elif user >= 7:
        print("HEAVY")
    
