print("------ Take 5 student names and their marks, then print average marks ------")
total_marks = 0

for i in range(5):
    name = input(f"Enter student {i+1} name: ")
    marks = float(input(f"Enter marks of {name}: "))
    total_marks += marks

average = total_marks / 5

print("Average marks of 5 students:", average)