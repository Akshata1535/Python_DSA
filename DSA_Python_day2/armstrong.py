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
    