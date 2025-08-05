students = []

while True:
    print("\nEnter student details:")
    name = input("Name: ")
    age = int(input("Age: "))
    major = input("Major: ")

    student = (name, age, major)
    students.append(student)

    cont = input("Do you want to add another student? (yes/no): ").lower()
    if cont != "yes":
        break

print("\nList of Students:")
for s in students:
    print(s)