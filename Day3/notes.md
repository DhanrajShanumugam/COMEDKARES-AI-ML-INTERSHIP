# Introduction to NumPy and Pandas

## 1. Introduction to NumPy

**NumPy** stands for **Numerical Python**.

It is a Python library mainly used for:

* Numerical calculations
* Working with arrays
* Mathematical operations
* Linear algebra
* Statistics
* Scientific computing
* Data processing

NumPy is faster and more efficient than normal Python lists when working with large amounts of numerical data.

---

# 2. Installing NumPy

NumPy can be installed using `pip`.

```bash
pip install numpy
```

If you are using a specific Python version:

```bash
py -3.12 -m pip install numpy
```

---

# 3. Importing NumPy

The standard way to import NumPy is:

```python
import numpy as np
```

`np` is an alias commonly used for NumPy.

---

# 4. Creating a NumPy Array

A NumPy array can be created using `np.array()`.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
```

Output:

```text
[10 20 30 40 50]
```

---

# 5. Accessing NumPy Array Elements

NumPy arrays use zero-based indexing.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers[0])
print(numbers[2])
print(numbers[-1])
```

Output:

```text
10
30
50
```

---

# 6. NumPy Array Operations

One of the main advantages of NumPy is that mathematical operations can be performed directly on arrays.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
```

Output:

```text
[5 7 9]
[-3 -3 -3]
[ 4 10 18]
```

---

# 7. Sum of Array Elements

NumPy provides the `sum()` function.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(np.sum(numbers))
```

Output:

```text
150
```

---

# 8. Mean of Array

The `mean()` function calculates the average.

```python
import numpy as np

marks = np.array([80, 90, 70, 60, 100])

print(np.mean(marks))
```

Output:

```text
80.0
```

---

# 9. Maximum and Minimum

NumPy provides `max()` and `min()`.

```python
import numpy as np

numbers = np.array([10, 25, 5, 40, 15])

print(np.max(numbers))
print(np.min(numbers))
```

Output:

```text
40
5
```

---

# 10. Shape of an Array

The `shape` attribute tells us the dimensions of an array.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])

print(numbers.shape)
```

Output:

```text
(4,)
```

This means the array contains 4 elements.

---

# 11. Two-Dimensional NumPy Array

NumPy can also create matrices or two-dimensional arrays.

```python
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

Accessing an element:

```python
print(matrix[0][1])
```

Output:

```text
2
```

---

# 12. Simple NumPy Program – Student Marks

```python
import numpy as np

marks = np.array([85, 90, 78, 92, 88])

print("Marks:", marks)
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
```

Output:

```text
Marks: [85 90 78 92 88]
Total: 433
Average: 86.6
Highest: 92
Lowest: 78
```

---

# 13. Introduction to Pandas

**Pandas** is a Python library used for:

* Data analysis
* Data manipulation
* Working with tables
* Reading CSV files
* Cleaning data
* Filtering data
* Grouping data
* Handling missing data

Pandas is very commonly used in **Data Science, Machine Learning, and Artificial Intelligence**.

---

# 14. Installing Pandas

Install Pandas using:

```bash
pip install pandas
```

For Python 3.12:

```bash
py -3.12 -m pip install pandas
```

---

# 15. Importing Pandas

The standard way to import Pandas is:

```python
import pandas as pd
```

`pd` is the commonly used alias for Pandas.

---

# 16. Pandas Series

A **Series** is a one-dimensional data structure in Pandas.

Example:

```python
import pandas as pd

marks = pd.Series([80, 90, 70, 85])

print(marks)
```

Output:

```text
0    80
1    90
2    70
3    85
dtype: int64
```

The numbers on the left are the indexes.

---

# 17. Pandas DataFrame

A **DataFrame** is a two-dimensional table containing rows and columns.

Example:

```python
import pandas as pd

data = {
    "Name": ["Dhanraj", "Vinooj", "Rahul"],
    "Age": [20, 21, 19],
    "Marks": [90, 85, 88]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
      Name  Age  Marks
0  Dhanraj   20     90
1   Vinooj   21     85
2    Rahul   19     88
```

---

# 18. Accessing a Column

A column can be accessed using its name.

```python
print(df["Name"])
```

Output:

```text
0    Dhanraj
1     Vinooj
2      Rahul
Name: Name, dtype: object
```

Another example:

```python
print(df["Marks"])
```

---

# 19. Accessing a Row

The `iloc` method can be used to access rows using their index.

```python
print(df.iloc[0])
```

This displays the first row.

Example output:

```text
Name     Dhanraj
Age           20
Marks         90
Name: 0, dtype: object
```

---

# 20. Adding a New Column

We can easily add a new column to a DataFrame.

```python
df["Grade"] = ["A", "B", "A"]

print(df)
```

Output:

```text
      Name  Age  Marks Grade
0  Dhanraj   20     90     A
1   Vinooj   21     85     B
2    Rahul   19     88     A
```

---

# 21. Filtering Data

Pandas allows us to filter rows based on conditions.

For example, to find students with marks greater than 85:

```python
result = df[df["Marks"] > 85]

print(result)
```

Output:

```text
      Name  Age  Marks Grade
0  Dhanraj   20     90     A
2    Rahul   19     88     A
```

---

# 22. Finding Average

We can calculate the average of a column using `mean()`.

```python
print(df["Marks"].mean())
```

Output:

```text
87.66666666666667
```

---

# 23. Finding Maximum and Minimum

```python
print("Highest:", df["Marks"].max())
print("Lowest:", df["Marks"].min())
```

Output:

```text
Highest: 90
Lowest: 85
```

---

# 24. Reading a CSV File

Pandas is very useful for reading CSV files.

Suppose we have a file called:

```text
students.csv
```

We can read it using:

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df)
```

Pandas automatically converts the CSV data into a DataFrame.

---

# 25. Writing Data to a CSV File

A DataFrame can also be saved as a CSV file.

```python
df.to_csv("students_output.csv", index=False)
```

`index=False` prevents Pandas from writing the DataFrame index as an extra column.

---

# 26. Checking DataFrame Information

### `head()`

Displays the first five rows.

```python
print(df.head())
```

### `tail()`

Displays the last five rows.

```python
print(df.tail())
```

### `shape`

Returns the number of rows and columns.

```python
print(df.shape)
```

Example:

```text
(3, 3)
```

This means:

```text
3 rows
3 columns
```

### `columns`

Displays column names.

```python
print(df.columns)
```

---

# 27. Simple Pandas Program

```python
import pandas as pd

data = {
    "Name": ["Dhanraj", "Vinooj", "Rahul", "Anil"],
    "Age": [20, 21, 19, 22],
    "Marks": [90, 85, 88, 75]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nStudents with marks greater than 85:")
print(df[df["Marks"] > 85])
```

---

# 28. NumPy vs Pandas

| Feature        | NumPy                   | Pandas               |
| -------------- | ----------------------- | -------------------- |
| Main purpose   | Numerical computing     | Data analysis        |
| Main structure | Array                   | Series and DataFrame |
| Best for       | Mathematical operations | Tabular data         |
| Handles labels | Limited                 | Yes                  |
| CSV handling   | Not the main purpose    | Excellent            |
| Data cleaning  | Limited                 | Excellent            |
| Common alias   | `np`                    | `pd`                 |

---

# 29. NumPy and Pandas Together

NumPy and Pandas are often used together.

Example:

```python
import numpy as np
import pandas as pd

marks = np.array([80, 90, 75, 95])

df = pd.DataFrame({
    "Marks": marks
})

print(df)
print("Average:", np.mean(marks))
```

Output:

```text
   Marks
0     80
1     90
2     75
3     95

Average: 85.0
```

NumPy performs numerical operations, while Pandas organizes the data into a table.

---

# 30. Important Points to Remember

## NumPy

* NumPy means **Numerical Python**.
* It is mainly used for numerical and scientific computing.
* NumPy's main data structure is the `ndarray`.
* Use `import numpy as np`.
* `np.array()` creates an array.
* `np.sum()` calculates the total.
* `np.mean()` calculates the average.
* `np.max()` finds the maximum.
* `np.min()` finds the minimum.
* `.shape` gives the dimensions of an array.

## Pandas

* Pandas is used for data analysis and manipulation.
* Use `import pandas as pd`.
* A `Series` is one-dimensional.
* A `DataFrame` is two-dimensional.
* `pd.DataFrame()` creates a DataFrame.
* `pd.read_csv()` reads CSV files.
* `to_csv()` saves a DataFrame to a CSV file.
* `head()` displays the first rows.
* `tail()` displays the last rows.
* `mean()` calculates an average.
* Data can be filtered using conditions.

---

# 31. Final Example

```python
import numpy as np
import pandas as pd

# NumPy array
marks = np.array([85, 90, 78, 92, 88])

print("NumPy Array:")
print(marks)

print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))

# Pandas DataFrame
data = {
    "Name": ["Dhanraj", "Vinooj", "Rahul", "Anil", "Kiran"],
    "Marks": marks
}

df = pd.DataFrame(data)

print("\nStudent Data:")
print(df)

print("\nStudents scoring above 85:")
print(df[df["Marks"] > 85])
```

This simple program demonstrates how **NumPy can be used for numerical calculations** and **Pandas can be used to organize and analyze the same data**.


simple programs
 introduction about numpy,pandas and eg
