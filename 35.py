print("------ Create a list of 10 numbers and print sum and average of all numbers ------")
numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print("Sum of numbers:", total)
print("Average of numbers:", average)