import numpy as np
import pandas as pd

# 1. Generate marks randomly between 60 and 100
np.random.seed(1)

marks = np.random.randint(60, 101, (5, 3))

# Create DataFrame
df = pd.DataFrame(
    marks,
    columns=["Python Marks", "AI Marks", "ML Marks"],
    index=["Student 1", "Student 2", "Student 3", "Student 4", "Student 5"]
)

# 2 & 3. Calculate average marks for each student
df["Average"] = marks.mean(axis=1)

# 4. Add Result column
# Pass if Average >= 75, otherwise Fail
df["Result"] = np.where(df["Average"] >= 75, "Pass", "Fail")

# 5. Display final DataFrame
print("Final DataFrame:")
print(df)

# 6. Find topper and print their name
topper = df["Average"].idxmax()

print("\nTopper:", topper)
