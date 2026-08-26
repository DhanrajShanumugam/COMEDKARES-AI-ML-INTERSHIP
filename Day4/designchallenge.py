import numpy as np
import pandas as pd

# -----------------------------------------
# Student Performance Analysis System
# -----------------------------------------

# Student names
names = ["Dhanraj", "Vinooj", "Rahul", "Anil", "Kiran"]

# Subject marks
python_marks = np.array([85, 90, 78, 92, 88])
sql_marks = np.array([80, 85, 75, 89, 90])
ai_marks = np.array([90, 88, 80, 95, 85])

# Create DataFrame
students = pd.DataFrame({
    "Name": names,
    "Python": python_marks,
    "SQL": sql_marks,
    "AI": ai_marks
})

# Calculate Total Marks
students["Total"] = (
    students["Python"] +
    students["SQL"] +
    students["AI"]
)

# Calculate Average Marks
students["Average"] = students["Total"] / 3

# Function to assign grades
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

# Assign grades
students["Grade"] = students["Average"].apply(calculate_grade)

# Display complete student data
print("===== STUDENT PERFORMANCE =====")
print(students.to_string(index=False))

# -----------------------------------------
# Overall Statistics
# -----------------------------------------

print("\n===== OVERALL STATISTICS =====")

print("Highest Total Marks:",
      np.max(students["Total"]))

print("Lowest Total Marks:",
      np.min(students["Total"]))

print("Average of All Students:",
      np.mean(students["Average"]))

# -----------------------------------------
# Students Above Average
# -----------------------------------------

overall_average = np.mean(students["Average"])

print("\n===== STUDENTS ABOVE AVERAGE =====")

above_average = students[
    students["Average"] > overall_average
]

print(above_average.to_string(index=False))

# -----------------------------------------
# Highest Scoring Student
# -----------------------------------------

highest_student = students.loc[
    students["Total"].idxmax()
]

print("\n===== TOP STUDENT =====")
print("Name:", highest_student["Name"])
print("Total Marks:", highest_student["Total"])
print("Average:", round(highest_student["Average"], 2))
print("Grade:", highest_student["Grade"])

output:
===== STUDENT PERFORMANCE =====

   Name  Python  SQL  AI  Total   Average Grade
Dhanraj      85   80  90    255 85.000000     A
 Vinooj      90   85  88    263 87.666667     A
  Rahul      78   75  80    233 77.666667     B
   Anil      92   89  95    276 92.000000    A+
  Kiran      88   90  85    263 87.666667     A

===== OVERALL STATISTICS =====
Highest Total Marks: 276

Lowest Total Marks: 233

Average of All Students: 86.00000000000001


===== STUDENTS ABOVE AVERAGE =====
  Name  Python  SQL  AI  Total   Average Grade
Vinooj      90   85  88    263 87.666667     A
  Anil      92   89  95    276 92.000000    A+
 Kiran      88   90  85    263 87.666667     A

===== TOP STUDENT =====
Name: Anil

Total Marks: 276

Average: 92.0

Grade: A+

Run completed in 3942ms
