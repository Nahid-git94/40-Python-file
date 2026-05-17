print("------ Find the largest number from a list of 10 numbers ------")
numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)