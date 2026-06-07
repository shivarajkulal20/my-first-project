class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print("-" * 25)


students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = Student(roll_no, name, marks)
        students.append(student)

        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                student.display()

    elif choice == "3":
        search_roll = input("Enter Roll Number to Search: ")
        found = False

        for student in students:
            if student.roll_no == search_roll:
                student.display()
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Try again.")