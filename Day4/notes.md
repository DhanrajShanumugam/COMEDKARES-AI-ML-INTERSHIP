# Advanced Concepts of Python

This section covers some important tools and libraries used in Python for **data analysis, numerical computing, experimentation, and machine learning**.

## Topics Covered

* NumPy
* Pandas
* Jupyter Notebook
* Google Colab

---

## 1. NumPy

**NumPy (Numerical Python)** is a Python library used for numerical and scientific computing.

### Main Features

* Multidimensional arrays
* Mathematical operations
* Statistical calculations
* Matrix operations
* Fast numerical processing

### Example

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
print("Sum:", np.sum(numbers))
print("Average:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
```

### Output

```text
[10 20 30 40 50]
Sum: 150
Average: 30.0
Maximum: 50
Minimum: 10
```

---

## 2. Pandas

**Pandas** is a Python library used for data analysis and data manipulation.

The two main Pandas data structures are:

* `Series` – One-dimensional data
* `DataFrame` – Two-dimensional tabular data

### Example

```python
import pandas as pd

data = {
    "Name": ["Dhanraj", "Vinooj", "Rahul"],
    "Marks": [90, 85, 88]
}

df = pd.DataFrame(data)

print(df)
```

### Output

```text
      Name  Marks
0  Dhanraj     90
1   Vinooj     85
2    Rahul     88
```

### Filtering Data

```python
print(df[df["Marks"] > 85])
```

This displays students whose marks are greater than 85.

---

## 3. Jupyter Notebook

**Jupyter Notebook** is an interactive environment used for writing and executing Python code.

It is commonly used for:

* Learning Python
* Data analysis
* Data visualization
* Machine learning
* Experiments
* Documentation

Jupyter Notebook allows us to combine:

* Python code
* Output
* Text
* Mathematical equations
* Charts and visualizations

### Example

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

np.mean(numbers)
```

The output is displayed directly below the code cell.

### Installing Jupyter

```bash
pip install notebook
```

### Starting Jupyter Notebook

```bash
jupyter notebook
```

A browser window will normally open with the Jupyter Notebook interface.

---

## 4. Google Colab

**Google Colab (Google Colaboratory)** is a cloud-based environment for writing and executing Python code.

It is especially useful because Python programs can be executed without setting up a complete Python environment locally.

### Advantages of Google Colab

* Runs in a web browser
* No complicated local setup required
* Supports Python
* Can install Python libraries
* Supports data analysis
* Supports machine learning
* Can use GPU/TPU resources when available
* Notebooks can be stored and shared through Google Drive

### Example

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(np.mean(numbers))
```

Output:

```text
30.0
```

### Installing a Library in Colab

A Python package can be installed using:

```python
!pip install numpy
```

Many common libraries are already available in Colab.

---

# 5. NumPy + Pandas Example

NumPy and Pandas are often used together.

```python
import numpy as np
import pandas as pd

marks = np.array([85, 90, 78, 92, 88])

data = {
    "Name": ["Dhanraj", "Vinooj", "Rahul", "Anil", "Kiran"],
    "Marks": marks
}

df = pd.DataFrame(data)

print(df)

print("\nAverage Marks:", np.mean(marks))

print("\nStudents with marks above 85:")
print(df[df["Marks"] > 85])
```

### Output

```text
      Name  Marks
0  Dhanraj     85
1   Vinooj     90
2    Rahul     78
3     Anil     92
4    Kiran     88

Average Marks: 86.6

Students with marks above 85:
      Name  Marks
1   Vinooj     90
3     Anil     92
4    Kiran     88
```

---

# 6. Comparison

| Tool             | Main Purpose                   |
| ---------------- | ------------------------------ |
| NumPy            | Numerical computing and arrays |
| Pandas           | Data analysis and tabular data |
| Jupyter Notebook | Interactive Python development |
| Google Colab     | Cloud-based Python development |

---

# 7. Key Takeaways

* **NumPy** is mainly used for numerical operations and arrays.
* **Pandas** is mainly used for data analysis and manipulation.
* **Jupyter Notebook** provides an interactive environment for Python.
* **Google Colab** provides a cloud-based Python environment.
* NumPy and Pandas are widely used in **Data Science, AI, and Machine Learning**.
* Jupyter and Google Colab are useful for experimenting with and documenting Python programs.

