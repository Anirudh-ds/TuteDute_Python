
students = {'Alan' : 78, 'Taylor' : 85, 'Haya' : 60, 'Xavier': 90, 'Chou': 83}

print("Enter student name : ", end="")
str = input()

if(str in students):
    print(f"{str}'s marks : {students[str]}")
else:
    print("Student not found.")
