num = input("enter an interger: ")
sumd = 0
for n in num:
    sumd += int(n) ** len(num)
if sumd == num:
    print(f'{num} is an a numebr')
else:
    print(f'{num} is not a number')