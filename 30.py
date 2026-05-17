print("------ Find the smallest number from a list of 10 numbers ------")
numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("smallest number is:", smallest)