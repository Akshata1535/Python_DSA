#armstrong number
num = int(input("Enter a number: "))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum + digit * digit * digit
    temp = temp // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not Armstrong number")

#armstrong2
number= 153
sum = 0
t1 = number
while t1>0:
    rem = t1%10
    sum+= rem**3
    t1//=10
if sum == number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
