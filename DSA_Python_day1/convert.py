
#convert temperature from celsius to fahrenheit
celsius = float(input("enter temperature in celsius"))      
fahrenheit = (celsius * 9/5) + 32
print("Temperature in fahrenheit is:", fahrenheit)
    
#calculate simple interest
principal = float(input("enter principal amount"))
rate = float(input("enter rate of interest"))   
time = float(input("enter time in years"))
simple_interest = (principal * rate * time) / 100
print("Simple Interest is:", simple_interest)


#swap two numbers
a = float(input("Enter value of a:"))
b = float(input("Enter value of b:"))
a,b = b,a
print("value of a is :",b)
print("value of b is :",a)


#find square of a number
num = float("Enter a number:")
square = num**2
print("Square of the number is:", square)



#find cube of a number
num = int(input("Enter a number:"))
cube = num**3
print("Cube of the number is:", cube)

#calculate average of three numbers
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
average = (num1 + num2 + num3) / 3
print("Average of the three numbers is:", average)

#convert kilometers to meters
kilometers = float(input("Enter distance in kilometers:"))  
meters = kilometers * 1000
print("Distance in meters is:", meters)


#convert rupees to dollars
rupees = float(input("Enter amount in rupees:"))
exchange_rate = 0.013  # Example exchange rate
dollars = rupees * exchange_rate
print("Amount in dollars is:", dollars)

#calculate percentage and total marks
marks_obtained = float(input("Enter marks obtained:"))  
total_marks = float(input("Enter total marks:"))
percentage = (marks_obtained / total_marks) * 100
print("Percentage is:", percentage)

write a python program to take a users name and age a input and print a message like
"Hello [name], you are [age] years old."
name = input("Enter your name:")
age = input("Enter your age:")
print(f"Hello {name}, you are {age} years old.")



write a program to calculate the area os a triabgle using the formula area = base * height / 2
base = float(input("Enter the base of the triangle:"))
height = float(input("Enter the height of the triangle:"))
area = (base * height) / 2
print("Area of the triangle is:", area)


wap to calculate the total number of students in a class by taking the number of boys and girls
boys = int(input("Enter the number of boys:"))  
girls = int(input("Enter the number of girls:"))
total_students = boys + girls   
print("Total number of students in the class is:", total_students)
