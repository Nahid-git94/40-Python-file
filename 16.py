print("------ Reverse a given number (e.g., 12345 → 54321) ------") ### Can't understand
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number =", reverse)