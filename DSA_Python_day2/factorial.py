#find factorial  of a number
range1= 7
factorial=1
for i in range (1, range1+1):
    factorial= factorial*i
    print(factorial)
#find factorial of a number
num = int(input("Enter a number:"))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("Factorial of", num, "is", factorial)

#print multiplication table of a number
num = int(input("Enter a number:"))
print("Multiplication table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#print multiplication table form 1- 1 and 11-  20 column wise
num = int(input("Enter a number:"))
print("Multiplication table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)



#fibonacci series
n = int(input("Enter the number of terms:"))
a, b = 0, 1
print("Fibonacci sequence:")
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b

#armstrong number
num = int(input("Enter a number:"))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")   
#prime number
num = int(input("Enter a number:"))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

#palindrome number or string
s = input("Enter a string or number:")
if s == s[::-1]:
    print(s, "is a palindrome.")
else:
    print(s, "is not a palindrome.")
    