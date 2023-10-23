# Exceptions

## Tasks

### 0. Safe list printing

**Mandatory**

Write a function that prints `x` elements of a list.

**Prototype:** `def safe_print_list(my_list=[], x=0):`

- `my_list` can contain any type (integer, string, etc.).
- All elements must be printed on the same line followed by a new line.
- `x` represents the number of elements to print.
- `x` can be bigger than the length of `my_list`.
- Returns the real number of elements printed.
- You have to use `try:/ except:`.
- You are not allowed to import any module.
- You are not allowed to use `len()`.

Example usage:

```python
my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
```

### 1. Safe printing of an integers list

**Mandatory**

Write a function that prints an integer with `"{:d}".format()`.

**Prototype:** `def safe_print_integer(value):`

- `value` can be any type (integer, string, etc.).
- The integer should be printed followed by a new line.
- Returns `True` if the value has been correctly printed (it means the value is an integer).
- Otherwise, returns `False`.
- You have to use `try:/ except:`.
- You have to use `"{:d}".format()` to print as an integer.
- You are not allowed to import any module.
- You are not allowed to use `type()`.

Example usage:

```python
value = 89
has_been printed = safe_print_integer(value)
if not has_been_printed:
    print("{} is not an integer".format(value))
```

### 2. Print and count integers

**Mandatory**

Write a function that prints the first `x` elements of a list and only integers.

**Prototype:** `def safe_print_list_integers(my_list=[], x=0):`

- `my_list` can contain any type (integer, string, etc.).
- All integers have to be printed on the same line followed by a new line; other types of values in the list must be skipped (silently).
- `x` represents the number of elements to access in `my_list`.
- `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur.
- Returns the real number of integers printed.
- You have to use `try:/ except:`.
- You have to use `"{:d}".format()` to print an integer.
- You are not allowed to import any module.
- You are not allowed to use `len()`.

Example usage:

```python
my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))
```

### 3. Integers division with debug

**Mandatory**

Write a function that divides two integers and prints the result.

**Prototype:** `def safe_print_division(a, b):`

- You can assume that `a` and `b` are integers.
- The result of the division should print on the `finally:` section preceded by `Inside result:`.
- Returns the value of the division; otherwise: `None`.
- You have to use `try:/ except:/ finally:`.
- You have to use `"{}".format()` to print the result.
- You are not allowed to import any module.

Example usage:

```python
a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
```

### 4. Divide a list

**Mandatory**

Write a function that divides element by element two lists.

**Prototype:** `def list_division(my_list_1, my_list_2, list_length):`

- `my_list_1` and `my_list_2` can contain any type (integer, string, etc.).
- `list_length` can be bigger than the length of both lists.
- Returns a new list (length = `list_length`) with all divisions.
- If two elements can’t be divided, the division result should be equal to 0.
- If an element is not an integer or float, print: `wrong type`.
- If the division can’t be done (`/0`), print: `division by 0`.
- If `my_list_1` or `my_list_2` is too short, print: `out of range`.
- You have to use `try:/ except:/ finally:`.
- You are not allowed to import any module.

Example usage:

```python
my_list_1 = [10, 8, 4]
my_list_2 = [2, 4, 4]
result = list_division(my_list_1, my_list_2, max(len(my_list_1), len(my_list_2)))
print(result)
```

### 5. Raise exception

**

Mandatory**

Write a function that raises a type exception.

**Prototype:** `def raise_exception():`

- You are not allowed to import any module.

Example usage:

```python
try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
```

### 6. Raise a message

**Mandatory**

Write a function that raises a name exception with a message.

**Prototype:** `def raise_exception_msg(message=""):`

- You are not allowed to import any module.

Example usage:

```python
try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
```

