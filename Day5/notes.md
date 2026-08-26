# Module 1: Python Programming

## Advanced Python Concepts

### Topics Covered

* Matplotlib
* Seaborn
* File Handling
* Important Python Libraries
* SVG and Vector Graphics

---

# 1. Matplotlib

**Matplotlib** is a popular Python library used for **data visualization**.

It can be used to create:

* Line charts
* Bar charts
* Pie charts
* Histograms
* Scatter plots
* Custom graphs

Matplotlib is commonly used together with NumPy and Pandas.

---

## 1.1 Installing Matplotlib

```bash
pip install matplotlib
```

For Python 3.12:

```bash
py -3.12 -m pip install matplotlib
```

---

## 1.2 Importing Matplotlib

The commonly used module is `pyplot`.

```python
import matplotlib.pyplot as plt
```

`plt` is the standard alias for `matplotlib.pyplot`.

---

# 2. Simple Line Chart

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 180, 200]

plt.plot(months, sales)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
```

This creates a line graph showing how sales change over time.

---

# 3. Bar Chart

A bar chart is useful for comparing different categories.

```python
import matplotlib.pyplot as plt

subjects = ["Python", "SQL", "AI", "Math"]
marks = [85, 90, 88, 78]

plt.bar(subjects, marks)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()
```

---

# 4. Scatter Plot

A scatter plot shows the relationship between two variables.

```python
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 60, 65, 75, 85]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()
```

---

# 5. Histogram

A histogram shows the distribution of numerical data.

```python
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 72, 75, 80, 85, 90, 95]

plt.hist(marks, bins=5)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()
```

---

# 6. Seaborn

**Seaborn** is a Python visualization library built on top of Matplotlib.

It provides a high-level interface for creating attractive and informative statistical graphs.

Seaborn is especially useful when working with **Pandas DataFrames**.

---

## 6.1 Installing Seaborn

```bash
pip install seaborn
```

For Python 3.12:

```bash
py -3.12 -m pip install seaborn
```

---

## 6.2 Importing Seaborn

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

---

# 7. Seaborn Bar Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Subject": ["Python", "SQL", "AI", "Math"],
    "Marks": [85, 90, 88, 78]
}

sns.barplot(x="Subject", y="Marks", data=data)

plt.title("Subject-wise Marks")
plt.show()
```

---

# 8. Seaborn Scatter Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 60, 65, 75, 85]

sns.scatterplot(x=hours, y=marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()
```

---

# 9. Seaborn Heatmap

A heatmap represents values using different levels of shading.

It is commonly used to display correlations.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Python": [85, 90, 78, 92],
    "SQL": [80, 85, 75, 89],
    "AI": [90, 88, 80, 95]
}

df = pd.DataFrame(data)

correlation = df.corr()

sns.heatmap(correlation, annot=True)

plt.title("Subject Correlation")
plt.show()
```

---

# 10. File Handling in Python

**File handling** allows Python programs to create, read, write, and modify files.

Common file operations include:

* Opening a file
* Reading a file
* Writing to a file
* Appending data
* Closing a file

---

# 11. Opening a File

Python uses the `open()` function.

### Syntax

```python
open(filename, mode)
```

Common modes:

| Mode | Purpose           |
| ---- | ----------------- |
| `r`  | Read              |
| `w`  | Write             |
| `a`  | Append            |
| `x`  | Create a new file |
| `rb` | Read binary       |
| `wb` | Write binary      |

---

# 12. Reading a File

Suppose we have a file called `students.txt`.

```python
file = open("students.txt", "r")

content = file.read()

print(content)

file.close()
```

---

# 13. Using `with open()`

A better way to handle files is using the `with` statement.

```python
with open("students.txt", "r") as file:
    content = file.read()

print(content)
```

The file is automatically closed after the block finishes.

---

# 14. Writing to a File

The `w` mode writes data to a file.

```python
with open("students.txt", "w") as file:
    file.write("Dhanraj\n")
    file.write("Vinooj\n")
    file.write("Rahul\n")
```

If the file does not exist, Python creates it.

**Important:** `w` mode replaces existing content.

---

# 15. Appending to a File

The `a` mode adds new content to the end of an existing file.

```python
with open("students.txt", "a") as file:
    file.write("Anil\n")
```

Existing content is not removed.

---

# 16. Reading Lines

The `readlines()` method reads all lines into a list.

```python
with open("students.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

We can also process each line:

```python
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())
```

`strip()` removes extra whitespace and the newline character.

---

# 17. Important Python Libraries

Python has a large ecosystem of libraries.

Some important libraries are:

| Library       | Main Use                           |
| ------------- | ---------------------------------- |
| NumPy         | Numerical computing                |
| Pandas        | Data analysis                      |
| Matplotlib    | Data visualization                 |
| Seaborn       | Statistical visualization          |
| Scikit-learn  | Machine learning                   |
| TensorFlow    | Machine learning and deep learning |
| PyTorch       | Deep learning                      |
| OpenCV        | Computer vision                    |
| Requests      | HTTP/API requests                  |
| BeautifulSoup | Web scraping                       |
| Flask         | Web development                    |
| Django        | Web development                    |

---

# 18. NumPy

NumPy stands for **Numerical Python**.

It provides efficient arrays and mathematical operations.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])

print(np.mean(numbers))
print(np.sum(numbers))
```

---

# 19. Pandas

Pandas is mainly used for data manipulation and analysis.

```python
import pandas as pd

data = {
    "Name": ["Dhanraj", "Vinooj"],
    "Marks": [90, 85]
}

df = pd.DataFrame(data)

print(df)
```

---

# 20. Combining Pandas and Matplotlib

Pandas can be used to organize data, while Matplotlib can visualize it.

```python
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Dhanraj", "Vinooj", "Rahul"],
    "Marks": [90, 85, 78]
}

df = pd.DataFrame(data)

plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.show()
```

---

# 21. SVG – Scalable Vector Graphics

**SVG** stands for **Scalable Vector Graphics**.

SVG is a vector image format used for:

* Icons
* Diagrams
* Charts
* Logos
* Web graphics
* Technical illustrations

Unlike raster images such as JPG and PNG, SVG graphics can be scaled without losing quality.

---

## 21.1 Saving a Matplotlib Graph as SVG

Matplotlib can directly save a graph in SVG format.

```python
import matplotlib.pyplot as plt

subjects = ["Python", "SQL", "AI"]
marks = [85, 90, 88]

plt.bar(subjects, marks)

plt.title("Student Marks")

plt.savefig("student_marks.svg", format="svg")

plt.show()
```

This creates:

```text
student_marks.svg
```

---

# 22. Simple File + Pandas + Matplotlib Project

Suppose we have a CSV file called `students.csv`.

Example:

```text
Name,Python,SQL,AI
Dhanraj,85,80,90
Vinooj,90,85,88
Rahul,78,75,80
Anil,92,89,95
```

We can read and visualize it:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("students.csv")

# Calculate average
df["Average"] = (
    df["Python"] +
    df["SQL"] +
    df["AI"]
) / 3

print(df)

# Create chart
plt.bar(df["Name"], df["Average"])

plt.title("Student Average Marks")
plt.xlabel("Student")
plt.ylabel("Average Marks")

plt.show()
```

---

# 23. Key Points

### Matplotlib

* Used for creating graphs and charts.
* Provides detailed control over visualizations.
* Commonly imported as `plt`.

### Seaborn

* Built on top of Matplotlib.
* Useful for statistical visualization.
* Works well with Pandas DataFrames.
* Commonly imported as `sns`.

### File Handling

* `open()` is used to work with files.
* `r` reads files.
* `w` writes/replaces file content.
* `a` appends content.
* `with open()` is recommended for safe file handling.

### Important Libraries

* NumPy → Numerical operations
* Pandas → Data analysis
* Matplotlib → Visualization
* Seaborn → Statistical visualization
* Scikit-learn → Machine learning
* OpenCV → Computer vision

### SVG

* SVG means Scalable Vector Graphics.
* It is a vector graphics format.
* Matplotlib can save graphs as SVG files.
* SVG graphics can be scaled without losing quality.

