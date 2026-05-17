print("------ Reverse a string using loop (without using slicing) ------")
text = input("Enter a string: ")

reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text  # add each character in front

print("Reversed string:", reversed_text)
