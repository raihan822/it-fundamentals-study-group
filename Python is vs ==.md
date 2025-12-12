**QUESTION:** Why Python uses is not?

---

# Why Python Uses the Syntax `is not`

Python uses the syntax `is not` to check whether two variables **do not** refer to the same object in memory. This choice emphasizes readability and aligns with Python’s philosophy of being clear and intuitive.

---

## 1. English-Like Readability (The Zen of Python)

Python highly values readability, and the phrase `is not` closely mirrors natural English:

* **English:** “This object is not that object.”
* **Python:** `a is not b`

This is far more readable than the alternative C-style logical expression:

* `not a is b` — which is harder for humans to parse.

---

## 2. The Difference Between `is` and `==`

Understanding the distinction between identity and equality is essential:

| Operator | Meaning          | Checks                                    |
| -------- | ---------------- | ----------------------------------------- |
| `==`     | Equality         | Do they have the same **value**?          |
| `is`     | Identity         | Are they the **same object** in memory?   |
| `is not` | Inverse Identity | Are they **different objects** in memory? |
| `!=`     | Inequality       | Do they have **different values**?        |

### Example

```python
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a  # c refers to the same list as a

# Value comparison:
print(list_a == list_b)      # True — same contents

# Identity comparison:
print(list_a is list_b)      # False — different objects in memory
print(list_a is list_c)      # True — same exact object

# Using 'is not':
print(list_a is not list_b)  # True — different objects
print(list_a is not list_c)  # False — same object
```

---

## 3. A Special Case: Checking for `None`

The most common use of `is not` is checking whether a variable is **not** `None`.

`None` is a **singleton** in Python (only one instance exists), so identity checks (`is`, `is not`) are the correct and recommended approach.

```python
# Recommended:
if variable is not None:
    print("Variable has a value.")

# Possible but discouraged:
if variable != None:
    print("Variable has a value.")
```

---

## Summary

The syntax `is not` was deliberately chosen to be:

* **Readable**
* **Unambiguous**
* **Pythonic**

It provides a clear and direct way to express **the negation of object identity**.

---