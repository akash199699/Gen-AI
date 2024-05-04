number=int(input('Enter a number : '))
n=number
s=0
while number>0:
    r=number%10
    s=s+r
    number=number//10
    if number==0:
        break
if n%s==0:
        print(n,'is a John number')
else:
        print(n,'is not a John number')