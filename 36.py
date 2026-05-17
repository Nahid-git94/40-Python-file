print("------ Count how many numbers are greater than 50 in a list ------")
numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

count = 0

for num in numbers:
    if num > 50:
        count += 1

print("Numbers greater than 50:", count)