# Python Fundamentals

## 1. Introduction

Python is a high-level, interpreted, general-purpose programming language. It is widely used for:

* Web development
* Data science
* Artificial Intelligence and Machine Learning
* Automation
* Software development
* Scientific computing

Python is easy to learn because its syntax is simple and readable.

---

# 2. Python Data Types

A **data type** defines the kind of value that a variable can store.

Common Python data types include:

* `int` – Integer numbers
* `float` – Decimal numbers
* `str` – Text and characters
* `bool` – True or False values
* `list` – Collection of values
* `tuple` – Ordered, immutable collection
* `set` – Unordered collection of unique values
* `dict` – Key-value pairs

---

## 2.1 Integer (`int`)

The `int` data type is used to store **whole numbers without decimal points**.

### Examples

```python
age = 20
marks = 95
temperature = -5
```

Here:

```python
age = 20
```

`age` contains an integer value.

### Important points

* Integers can be positive or negative.
* Integers do not contain decimal points.
* Python integers can store very large numbers.

### Example

```python
x = 100
y = 50

print(x + y)
```

Output:

```text
150
```

---

# 2.2 Float (`float`)

The `float` data type is used to store **numbers containing decimal points**.

### Examples

```python
price = 99.50
height = 5.8
temperature = -2.5
```

For example:

```python
price = 99.50
```

The value of `price` is a floating-point number.

### Example

```python
x = 10.5
y = 2.5

print(x + y)
```

Output:

```text
13.0
```

### Important point

Python uses `float` for decimal values. Python does **not** have a separate `double` data type like C/C++ or Java.

---

# 2.3 String (`str`)

The `str` data type is used to store **text**.

A string can contain:

* Words
* Sentences
* Numbers represented as text
* Individual characters

### Examples

```python
name = "Dhanu"
city = "Bangalore"
character = "A"
```

In Python, `"A"` is a **string**, not a `char` data type.

### Important point

Python does **not** have a separate `char` data type.

For example:

```python
letter = "A"
```

The type of `letter` is:

```python
str
```

You can check the type using:

```python
print(type(letter))
```

Output:

```text
<class 'str'>
```

### Strings can use single or double quotes

```python
name = "Dhanu"
name = 'Dhanu'
```

Both are valid.

---

# 2.4 Boolean (`bool`)

The `bool` data type represents either:

```text
True
False
```

### Example

```python
is_student = True
is_admin = False
```

Boolean values are commonly used in conditions.

```python
age = 20

print(age >= 18)
```

Output:

```text
True
```

---

# 3. Variables

A variable is a name used to store a value.

### Syntax

```python
variable_name = value
```

### Examples

```python
age = 20
name = "Dhanu"
height = 5.8
is_student = True
```

Python automatically determines the data type.

```python
x = 10
```

Here, Python understands that `x` is an integer.

```python
x = 10.5
```

Now `x` is a float.

---

# 4. Operators in Python

Operators are symbols or keywords used to perform operations on values and variables.

Main types of operators are:

1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Membership operators
6. Identity operators

---

# 5. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Name           | Example   | Result |
| -------- | -------------- | --------- | ------ |
| `+`      | Addition       | `10 + 5`  | `15`   |
| `-`      | Subtraction    | `10 - 5`  | `5`    |
| `*`      | Multiplication | `10 * 5`  | `50`   |
| `/`      | Division       | `10 / 5`  | `2.0`  |
| `//`     | Floor Division | `10 // 3` | `3`    |
| `%`      | Modulus        | `10 % 3`  | `1`    |
| `**`     | Exponentiation | `2 ** 3`  | `8`    |

### Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

# 6. Assignment Operators

Assignment operators are used to assign or update values in variables.

## Basic Assignment

```python
a = 10
```

This means:

> Store the value `10` in the variable `a`.

---

## Addition Assignment (`+=`)

```python
a = 10
a += 5
```

This is equivalent to:

```python
a = a + 5
```

After this operation:

```text
a = 15
```

---

## Subtraction Assignment (`-=`)

```python
a = 10
a -= 3
```

Equivalent to:

```python
a = a - 3
```

Result:

```text
a = 7
```

---

## Multiplication Assignment (`*=`)

```python
a = 10
a *= 2
```

Equivalent to:

```python
a = a * 2
```

Result:

```text
a = 20
```

---

## Division Assignment (`/=`)

```python
a = 10
a /= 2
```

Equivalent to:

```python
a = a / 2
```

Result:

```text
a = 5.0
```

---

## Other Assignment Operators

| Operator | Equivalent To    |
| -------- | ---------------- |
| `=`      | `a = value`      |
| `+=`     | `a = a + value`  |
| `-=`     | `a = a - value`  |
| `*=`     | `a = a * value`  |
| `/=`     | `a = a / value`  |
| `//=`    | `a = a // value` |
| `%=`     | `a = a % value`  |
| `**=`    | `a = a ** value` |

---

# 7. Understanding `a = a + b`

Consider:

```python
a = 10
b = 5

a = a + b
```

Step-by-step:

1. `a` initially contains `10`.
2. `b` contains `5`.
3. Python calculates `a + b`.
4. `10 + 5 = 15`.
5. The result `15` is assigned back to `a`.

Therefore:

```text
a = 15
```

This can also be written as:

```python
a += b
```

Both produce the same result.

---

# 8. Comparison Operators

Comparison operators are used to compare two values.

They return either `True` or `False`.

| Operator | Meaning                  | Example  |
| -------- | ------------------------ | -------- |
| `==`     | Equal to                 | `a == b` |
| `!=`     | Not equal to             | `a != b` |
| `>`      | Greater than             | `a > b`  |
| `<`      | Less than                | `a < b`  |
| `>=`     | Greater than or equal to | `a >= b` |
| `<=`     | Less than or equal to    | `a <= b` |

### Example

```python
a = 10
b = 5

print(a > b)
```

Output:

```text
True
```

---

# 9. Logical Operators

Logical operators are used to combine conditions.

### `and`

Returns `True` when both conditions are true.

```python
age = 20

print(age >= 18 and age <= 60)
```

Output:

```text
True
```

### `or`

Returns `True` when at least one condition is true.

```python
age = 15

print(age < 18 or age > 60)
```

Output:

```text
True
```

### `not`

Reverses the result.

```python
is_student = True

print(not is_student)
```

Output:

```text
False
```

---

# 10. Membership Operators

Membership operators check whether a value exists inside a sequence.

### `in`

```python
name = "Dhanu"

print("D" in name)
```

Output:

```text
True
```

### `not in`

```python
name = "Dhanu"

print("x" not in name)
```

Output:

```text
True
```

---

# 11. Identity Operators

Identity operators check whether two variables refer to the same object.

### `is`

```python
a = [1, 2, 3]
b = a

print(a is b)
```

Output:

```text
True
```

### `is not`

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b)
```

Output:

```text
True
```

Note that `is` checks **object identity**, while `==` checks **value equality**.

---

# 12. Type Checking

Python provides the `type()` function to check the data type of a value.

```python
x = 10
print(type(x))
```

Output:

```text
<class 'int'>
```

Another example:

```python
x = 10.5
print(type(x))
```

Output:

```text
<class 'float'>
```

And:

```python
x = "Hello"
print(type(x))
```

Output:

```text
<class 'str'>
```

---

# 13. Type Conversion

Type conversion means converting a value from one data type to another.

### Integer to Float

```python
x = 10
y = float(x)

print(y)
```

Output:

```text
10.0
```

### Float to Integer

```python
x = 10.8
y = int(x)

print(y)
```

Output:

```text
10
```

The decimal portion is removed.

### String to Integer

```python
x = "100"
y = int(x)

print(y)
```

Output:

```text
100
```

### Integer to String

```python
x = 100
y = str(x)

print(y)
```

Output:

```text
100
```

---

# 14. Important Python Data Type Summary

| Data Type | Description                  | Example             |
| --------- | ---------------------------- | ------------------- |
| `int`     | Whole numbers                | `10`                |
| `float`   | Decimal numbers              | `10.5`              |
| `str`     | Text/characters              | `"Hello"`           |
| `bool`    | True/False                   | `True`              |
| `list`    | Ordered mutable collection   | `[1, 2, 3]`         |
| `tuple`   | Ordered immutable collection | `(1, 2, 3)`         |
| `set`     | Collection of unique values  | `{1, 2, 3}`         |
| `dict`    | Key-value pairs              | `{"name": "Dhanu"}` |

---

# 15. Key Points to Remember

* `int` stores whole numbers.
* `float` stores decimal/floating-point numbers.
* Python does not have a separate `double` data type; `float` is normally used for floating-point values.
* Python does not have a separate `char` data type.
* A single character such as `"A"` is a `str`.
* `bool` stores `True` or `False`.
* `=` is an assignment operator.
* `==` is a comparison operator used to check equality.
* `a = a + b` adds `b` to `a` and stores the result back in `a`.
* `a += b` is a shorter form of `a = a + b`.
* The `type()` function can be used to check the type of a value.
* Python supports automatic type detection for variables.

---

# 16. Simple Practice Program

```python
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

a = a + b

print("New value of a:", a)
print("Type of a:", type(a))
```

### Output

```text
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
New value of a: 15
Type of a: <class 'int'>
```

---

## Conclusion

Understanding Python data types, variables, and operators is one of the most important foundations of Python programming. These concepts are used in almost every Python program, from simple calculations to advanced Artificial Intelligence applications.


Python Fundamentals:
Data Type:
int(integer)it stores the decimal values,(float,double) it stores the decimal point values ,char(character) it has stores the single bit of characters 
operators, ( a=a+b )
