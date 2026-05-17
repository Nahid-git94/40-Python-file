print("------ Find sum of digits of a number (e.g., 1234 = 1+2+3+4 = 10) ------") ### Can't understand
num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print("Sum of digits =", sum)