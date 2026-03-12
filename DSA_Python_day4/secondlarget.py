#find second largest
num = [121,453,780,340,8900,1535]
maximum = second_max = float("-inf")
for i in num:
    if i>maximum:
        second_max=maximum
        maximum=i
    elif i>second_max and i!=maximum:
        second_max=i
print("Second largest number is:",second_max)