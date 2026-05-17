print("------ Create a dictionary of 5 students (name: marks) and print all names and marks? ------")
students = {}

for i in range(5):
    name = input(f"Enter student {i+1} name: ")
    marks = int(input(f"Enter marks of {name}: "))
    students[name] = marks

print("\nStudent Names and Marks:")

for name, marks in students.items():
    print(name, ":", marks)