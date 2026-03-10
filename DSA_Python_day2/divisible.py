#check divisible by 3 and 5
num = int(input("Enter a number"))
if num %3==0 and num%5==0:
    print(num,"is divisible by 3 and 5")
else:
    print(num,"is not divisible by 3 and 5")


# print numbers from 1 to N:(N is input by user)
N = int(input("Enter a number:"))
for i in range(1, N + 1):
    print(i)

#range 1- 40 ==> even odd
for i in range(1,41):
    if i %2 == 0:
        print(i,"is an even number")
    else:
        print(i,"is an odd number")
