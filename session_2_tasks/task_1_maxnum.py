#-----------------------------------------------------------
#code to find the largest item from a given list using loop.
#-----------------------------------------------------------

numbers = [1,2,33,4,55]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
        
print("largest number is :",max)



