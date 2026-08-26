import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
# STUDENT PERFORMANCE VISUALIZATION
# AND REPORT SYSTEM
# ==========================================


# 1. Read student data from CSV file
df = pd.read_csv("students.csv")

print("===== ORIGINAL STUDENT DATA =====")
print(df)


# 2. Calculate total marks
df["Total"] = (
    df["Python"] +
    df["SQL"] +
    df["AI"]
)


# 3. Calculate average marks
df["Average"] = df["Total"] / 3


# 4. Assign grades
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


df["Grade"] = df["Average"].apply(calculate_grade)


# 5. Display processed student data
print("\n===== STUDENT PERFORMANCE =====")
print(df.to_string(index=False))


# 6. NumPy calculations
averages = np.array(df["Average"])

highest_average = np.max(averages)
lowest_average = np.min(averages)
overall_average = np.mean(averages)

print("\n===== STATISTICS =====")
print("Highest Average:", round(highest_average, 2))
print("Lowest Average:", round(lowest_average, 2))
print("Overall Average:", round(overall_average, 2))


# 7. Find the highest scoring student
top_student = df.loc[df["Total"].idxmax()]

print("\n===== TOP STUDENT =====")
print("Name:", top_student["Name"])
print("Total Marks:", top_student["Total"])
print("Average:", round(top_student["Average"], 2))
print("Grade:", top_student["Grade"])


# 8. Find students above overall average
above_average = df[df["Average"] > overall_average]

print("\n===== STUDENTS ABOVE AVERAGE =====")

print(
    above_average[
        ["Name", "Average", "Grade"]
    ].to_string(index=False)
)


# ==========================================
# MATPLOTLIB VISUALIZATION
# ==========================================

plt.figure(figsize=(8, 5))

plt.bar(
    df["Name"],
    df["Average"]
)

plt.title("Student Average Marks")
plt.xlabel("Student")
plt.ylabel("Average Marks")

plt.xticks(rotation=30)

plt.tight_layout()

# Save graph as SVG
plt.savefig(
    "student_average.svg",
    format="svg"
)

plt.show()


# ==========================================
# SEABORN SUBJECT COMPARISON
# ==========================================

subjects = ["Python", "SQL", "AI"]

# Convert data into a format suitable for Seaborn
long_data = df.melt(
    id_vars="Name",
    value_vars=subjects,
    var_name="Subject",
    value_name="Marks"
)

plt.figure(figsize=(9, 5))

sns.barplot(
    data=long_data,
    x="Name",
    y="Marks",
    hue="Subject"
)

plt.title("Subject-wise Student Performance")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.xticks(rotation=30)

plt.tight_layout()

plt.show()


# ==========================================
# SEABORN CORRELATION HEATMAP
# ==========================================

correlation = df[
    ["Python", "SQL", "AI"]
].corr()

plt.figure(figsize=(6, 5))

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Subject Correlation")

plt.tight_layout()

plt.show()


# ==========================================
# SAVE ANALYZED DATA
# ==========================================

df.to_csv(
    "student_analysis.csv",
    index=False
)

print("\n===== FILES CREATED =====")
print("student_analysis.csv")
print("student_average.svg")

output:
===== ORIGINAL STUDENT DATA =====
      Name  Python  SQL  AI
0  Dhanraj      85   80  90
1   Vinooj      90   85  88
2    Rahul      78   75  80
3     Anil      92   89  95
4    Kiran      88   90  85


===== STUDENT PERFORMANCE =====
   Name  Python  SQL  AI  Total   Average Grade
Dhanraj      85   80  90    255     85.00     A
 Vinooj      90   85  88    263     87.67     A
  Rahul      78   75  80    233     77.67     B
   Anil      92   89  95    276     92.00    A+
  Kiran      88   90  85    263     87.67     A


===== STATISTICS =====
Highest Average: 92.0
Lowest Average: 77.67
Overall Average: 86.0


===== TOP STUDENT =====
Name: Anil
Total Marks: 276
Average: 92.0
Grade: A+


===== STUDENTS ABOVE AVERAGE =====
   Name  Average Grade
 Vinooj    87.67     A
   Anil    92.00    A+
  Kiran    87.67     A


===== FILES CREATED =====
student_analysis.csv
student_average.svg
