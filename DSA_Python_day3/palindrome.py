#palindrome number or string
s = input("Enter a string or number:")
if s == s[::-1]:
    print(s, "is a palindrome.")
else:
    print(s, "is not a palindrome.")
    