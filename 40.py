print("------  Take a list of numbers and create two new lists: one for even numbers and one for odd numbers ------")
numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
