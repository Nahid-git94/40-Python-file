print("------ Print all vowels from a given string ------")
text = input("Enter a string: ")

vowels = "aeiouAEIOU"

print("Vowels in the string are:")
for ab in text:
    if ab in vowels:
        print(ab)