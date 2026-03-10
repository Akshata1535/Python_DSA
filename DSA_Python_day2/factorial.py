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
#armstrong number
#prime number
#palindrome number or string