# Python Fundamentals – Functions and Data Structures

## 1. Functions

A **function** is a reusable block of code that performs a specific task.

Functions help us:

* Avoid repeating code
* Organize programs
* Make code easier to understand
* Reuse the same logic multiple times

---

## 1.1 Creating a Function

In Python, a function is created using the `def` keyword.

### Syntax

```python
def function_name(parameters):
    # function body
```

### Example

```python
def multiply(a, b):
    print(a * b)
    return a * b
```

Here:

* `def` is used to define a function.
* `multiply` is the function name.
* `a` and `b` are parameters.
* `print(a * b)` displays the result.
* `return a * b` sends the result back to the caller.

---

## 1.2 Calling a Function

A function is executed by calling its name.

```python
result = multiply(4, 5)
print(result)
```

### Execution

The function receives:

```text
a = 4
b = 5
```

Then:

```text
a * b = 4 * 5
      = 20
```

The function prints:

```text
20
```

It also returns `20`.

Therefore:

```python
result = 20
```

Then:

```python
print(result)
```

prints:

```text
20
```

### Output

```text
20
20
```

The first `20` comes from the `print()` inside the function.

The second `20` comes from:

```python
print(result)
```

---

# 2. Parameters and Arguments

A **parameter** is a variable defined in a function.

```python
def multiply(a, b):
    return a * b
```

Here `a` and `b` are parameters.

An **argument** is the actual value passed to the function.

```python
multiply(4, 5)
```

Here:

```text
4 and 5
```

are arguments.

---

# 3. Return Statement

The `return` statement sends a value back from a function.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

Without `return`, the function would not send the calculated result back to `result`.

---

# 4. List

A **list** is a collection of multiple values stored in a single variable.

Lists are:

* Ordered
* Mutable
* Allow duplicate values
* Written using square brackets `[]`

### Example

```python
car = ["Bmw", "audi", "ferrari", "rollsroyces", "jaguar"]
```

The list contains five elements.

---

# 4.1 List Indexing

Each element in a list has an index.

Python uses **zero-based indexing**.

For example:

```text
Index:    0       1        2          3           4
          ↓       ↓        ↓          ↓           ↓
        "Bmw"  "audi"  "ferrari"  "rollsroyces" "jaguar"
```

Therefore:

```python
print(car[2])
```

Output:

```text
ferrari
```

Because `ferrari` is at index `2`.

---

# 4.2 Adding an Element Using `append()`

The `append()` method adds an element to the end of a list.

```python
car.append("fortuner")
```

Before:

```python
["Bmw", "audi", "ferrari", "rollsroyces", "jaguar"]
```

After:

```python
["Bmw", "audi", "ferrari", "rollsroyces", "jaguar", "fortuner"]
```

---

# 4.3 Removing an Element Using `remove()`

The `remove()` method removes a specified value from a list.

```python
car.remove("jaguar")
```

Before:

```python
["Bmw", "audi", "ferrari", "rollsroyces", "jaguar", "fortuner"]
```

After:

```python
["Bmw", "audi", "ferrari", "rollsroyces", "fortuner"]
```

If the specified value does not exist, Python raises a `ValueError`.

---

# 4.4 Printing a List

```python
print(car)
```

This displays the complete list.

Example:

```text
['Bmw', 'audi', 'ferrari', 'rollsroyces', 'fortuner']
```

---

# 4.5 Complete List Example

```python
car = ["Bmw", "audi", "ferrari", "rollsroyces", "jaguar"]

print(car[2])

car.append("fortuner")
print(car)

car.remove("jaguar")
print(car)
```

Output:

```text
ferrari
['Bmw', 'audi', 'ferrari', 'rollsroyces', 'jaguar', 'fortuner']
['Bmw', 'audi', 'ferrari', 'rollsroyces', 'fortuner']
```

---

# 5. Tuple

A **tuple** is an ordered collection of values.

Tuples are:

* Ordered
* Immutable
* Allow duplicate values
* Written using parentheses `()`

### Example

```python
days = (
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
)
```

---

# 5.1 Tuple Indexing

Tuples use zero-based indexing just like lists.

```python
print(days[0])
```

Output:

```text
monday
```

The first element has index `0`.

---

# 5.2 Negative Indexing

Python also supports negative indexing.

```python
print(days[-1])
```

Output:

```text
sunday
```

`-1` refers to the last element.

Example:

```text
Index:    0        1         2          ...       6
         monday  tuesday  wednesday             sunday

Negative:
         -7       -6        -5         ...       -1
```

---

# 5.3 Finding the Length of a Tuple

The `len()` function returns the number of elements.

```python
print(len(days))
```

Output:

```text
7
```

---

# 5.4 List vs Tuple

| Feature             | List | Tuple |
| ------------------- | ---- | ----- |
| Brackets            | `[]` | `()`  |
| Ordered             | Yes  | Yes   |
| Mutable             | Yes  | No    |
| Can add elements    | Yes  | No    |
| Can remove elements | Yes  | No    |
| Duplicate values    | Yes  | Yes   |

### Example

List:

```python
cars = ["BMW", "Audi"]
cars.append("Ferrari")
```

Tuple:

```python
days = ("Monday", "Tuesday")
```

A tuple cannot be modified directly.

---

# 6. Dictionary

A **dictionary** stores data as **key-value pairs**.

Dictionaries are written using curly brackets `{}`.

### Example

```python
student = {
    "name": "Dhanraj",
    "usn": 1234,
    "branch": "CSE",
    "cgpa": 9.5
}
```

Here:

| Key        | Value       |
| ---------- | ----------- |
| `"name"`   | `"Dhanraj"` |
| `"usn"`    | `1234`      |
| `"branch"` | `"CSE"`     |
| `"cgpa"`   | `9.5`       |

---

# 6.1 Accessing Dictionary Values

We can access a value using its key.

```python
print(student["name"])
```

Output:

```text
Dhanraj
```

Another example:

```python
print(student["cgpa"])
```

Output:

```text
9.5
```

---

# 6.2 Looping Through a Dictionary

The `items()` method returns both keys and values.

```python
for key, value in student.items():
    print(key, ":", value)
```

Output:

```text
name : Dhanraj
usn : 1234
branch : CSE
cgpa : 9.5
```

This is useful when we want to process every key-value pair.

---

# 7. Student Management System

We can combine:

* Functions
* Lists
* Tuples
* Dictionaries
* Loops

to create a simple student management system.

---

## 7.1 Subjects Tuple

We can store subjects in a tuple:

```python
subjects = ("python", "sql", "ai")
```

Since the subjects are fixed, a tuple is suitable.

---

## 7.2 Students List

We create a list to store multiple students.

```python
students = []
```

Each student can be represented using a dictionary.

Example:

```python
{
    "name": "Dhanraj",
    "age": 20,
    "subjects": ("python", "sql", "ai")
}
```

---

# 7.3 Adding Students Using a Function

We can create a function called `add_student()`.

```python
students = []

subjects = ("python", "sql", "ai")

def add_student(name, age):
    student_details = {
        "name": name,
        "age": age,
        "subjects": subjects
    }

    students.append(student_details)
```

The function receives:

```text
name
age
```

and creates a dictionary containing the student's information.

---

# 7.4 Adding Students

We can now call the function:

```python
add_student("Dhanraj", 20)
add_student("Vinooj", 21)
```

This creates two student records.

---

# 7.5 Displaying Students

We can use a `for` loop:

```python
for student_details in students:
    print(student_details)
```

Output:

```text
{'name': 'Dhanraj', 'age': 20, 'subjects': ('python', 'sql', 'ai')}
{'name': 'Vinooj', 'age': 21, 'subjects': ('python', 'sql', 'ai')}
```

---

# 7.6 Complete Student Management Program

```python
subjects = ("python", "sql", "ai")

students = []


def add_student(name, age):
    student_details = {
        "name": name,
        "age": age,
        "subjects": subjects
    }

    students.append(student_details)


add_student("Dhanraj", 20)
add_student("Vinooj", 21)


for student_details in students:
    print(student_details)
```

### Output

```text
{'name': 'Dhanraj', 'age': 20, 'subjects': ('python', 'sql', 'ai')}
{'name': 'Vinooj', 'age': 21, 'subjects': ('python', 'sql', 'ai')}
```

---

# 8. Understanding the Student Management System

The program uses several Python concepts together.

### Tuple

```python
subjects = ("python", "sql", "ai")
```

Stores the fixed list of subjects.

### List

```python
students = []
```

Stores multiple student records.

### Function

```python
def add_student(name, age):
```

Creates a reusable way to add students.

### Dictionary

```python
student_details = {
    "name": name,
    "age": age,
    "subjects": subjects
}
```

Stores information about one student.

### `append()`

```python
students.append(student_details)
```

Adds the student dictionary to the students list.

### Loop

```python
for student_details in students:
    print(student_details)
```

Iterates through all student records.

---

# 9. Important Methods and Functions

## List Methods

| Method      | Purpose                          |
| ----------- | -------------------------------- |
| `append()`  | Adds an element                  |
| `remove()`  | Removes a specified element      |
| `pop()`     | Removes an element by index      |
| `insert()`  | Inserts an element at a position |
| `sort()`    | Sorts the list                   |
| `reverse()` | Reverses the list                |
| `clear()`   | Removes all elements             |

---

## Dictionary Methods

| Method     | Purpose                   |
| ---------- | ------------------------- |
| `keys()`   | Returns all keys          |
| `values()` | Returns all values        |
| `items()`  | Returns key-value pairs   |
| `get()`    | Gets a value using a key  |
| `update()` | Updates dictionary values |
| `pop()`    | Removes a key-value pair  |

Example:

```python
student = {
    "name": "Dhanraj",
    "age": 20
}

print(student.keys())
print(student.values())
print(student.items())
```

---

# 10. Key Points to Remember

* A **function** is a reusable block of code.
* `def` is used to define a function.
* Parameters receive values passed to a function.
* `return` sends a value back from a function.
* A **list** is ordered and mutable.
* A **tuple** is ordered and immutable.
* A **dictionary** stores key-value pairs.
* List indexing starts from `0`.
* Negative index `-1` refers to the last element.
* `append()` adds an element to a list.
* `remove()` removes a specified element from a list.
* `len()` returns the number of elements.
* `items()` is useful for looping through dictionary key-value pairs.
* Functions, lists, tuples, and dictionaries can be combined to create useful programs.

---

# 11. Practice Exercise

Try creating a student management program that can:

1. Add a student
2. Display all students
3. Store student name and age
4. Store subjects
5. Store CGPA
6. Display each student's information

Example student:

```python
{
    "name": "Dhanraj",
    "age": 20,
    "subjects": ("python", "sql", "ai"),
    "cgpa": 9.5
}
```

This exercise will help you practice **functions, lists, tuples, dictionaries, loops, and variables together**.


-->functions:
def multiply(a,b):
     print(a*b)
     return a*b
result=multiply(4,5)
print(result)
list:
car=["Bmw","audi","ferrari","rollsroyces","jaguar"]
print(car[2])
car.append("fortuner")
print(car)
car.remove("jaguar")
print(car)
print(car)
tuple:
days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
print(days[0])
print(days[-1])
print(len(days))
dictionary:
student={
    "name":"dhanraj",
    "usn":1234,
    "branch":"CSE",
    "cgpa":9.5
}
for key,value in student.items():
    print(key,":",value)
    
    -->student management system:
    subjects=("python","sql","ai")
student=[]
def add_student(name,age):
    student_details={
        "name":"dhanraj",
        "age":20,
        "subject":subjects
    }
    student.append(student_details)
add_student("name","age")    
#add_student("Dhanraj",20)
#add_student("vinooj",21)
for student_details in student:
    print(student_details)
        
    
