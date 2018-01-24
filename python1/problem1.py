#init list
numbers = []

# check each number
for i in range(2000, 5001):
    if i%7==0 and i%5!=0:
        numbers.append(i) #add to list if condition is met

print(numbers)

