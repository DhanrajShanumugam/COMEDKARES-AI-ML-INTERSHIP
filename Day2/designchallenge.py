Student Management System (Python)

Objective

Learn how to: 1. Create a tuple of three subjects. 2. Create an emptylist called students. 3. Write a function add_student(name, age).

Python Program

# 1. Create a tuple of three subjects
subjects = ("Python", "Mathematics", "English")

# 2. Create an empty list called students
students = []

# 3. Function to add a student
def add_student(name, age):
    student = {
        "Name": name,
        "Age": age,
        "Subjects": subjects
    }
    students.append(student)
    print("Student added successfully!")

# Example
add_student("Vijay", 20)
add_student("Rahul", 19)

print("\nStudent Records:")
for student in students:
    print(student)

Explanation

Tuple (subjects): Stores the three subjects. Tuples areimmutable.

List (students): Stores multiple student records.

Dictionary (student): Stores one student's details.

Function (add_student): Creates a dictionary and adds it tothe students list.

Sample Output

Student added successfully!
Student added successfully!

Student Records:
{'Name': 'Vijay', 'Age': 20, 'Subjects': ('Python', 'Mathematics', 'English')}
{'Name': 'Rahul', 'Age': 19, 'Subjects': ('Python', 'Mathematics', 'English')}
