## Tasks

### 0. Import a Simple Function from a Simple File
```python
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)
```

Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

- You have to use the `print` function with string format to display integers.
- You have to assign:
  - the value `1` to a variable called `a`
  - the value `2` to a variable called `b`
  - and use those two variables as arguments when calling the functions `add` and `print`.
- `a` and `b` must be defined in 2 different lines: `a = 1` and another `b = 2`.
- Your program should print: `<a value> + <b value> = <add(a, b) value>` followed by a new line.
- You can only use the word `add_0` once in your code.
- You are not allowed to use `*` for importing or `__import__`.
- Your code should not be executed when imported.

### 1. My First Toolbox!
```python
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)

def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)

def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)
```

Write a program that imports functions from the file `calculator_1.py`, performs mathematical operations, and prints the result.

- Do not use the `print` function (with string format to display integers) more than 4 times.
- You have to define:
  - the value `10` to a variable `a`
  - the value `5` to a variable `b`
  - and use those two variables only as arguments when calling functions (including `print`).
- `a` and `b` must be defined in 2 different lines: `a = 10` and another `b = 5`.
- Your program should call each of the imported functions.

### 2. How to Make a Script Dynamic!
Write a program that prints the number of and the list of its arguments.

The output should be:
- "Number of argument(s)" followed by "argument" (if number is one) or "arguments" (otherwise), followed by ": (or . if no arguments were passed)" followed by a new line.
- (if at least one argument) one line per argument:
  - the position of the argument (starting at 1) followed by ":", followed by the argument value and a new line.

Your code should not be executed when imported.

### 3. Infinite Addition
Write a program that prints the result of the addition of all arguments.

The output should be the result of the addition of all arguments, followed by a new line.

You can cast arguments into integers by using `int()` (you can assume that all arguments can be casted into integers).

Your code should not be executed when imported.

### 4. Who Are You?
Write a program that prints all the names defined by the compiled module `hidden_4.pyc` (please download it locally).

You should print one name per line, in alphabetical order.

You should print only names that do not start with `__`.

Your code should not be executed when imported.

Make sure you are running your code in Python3.8.x (hidden_4.pyc has been compiled with this version).

### 5. Everything Can Be Imported
Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.

You are not allowed to use `*` for importing or `__import__`.

Your code should not be executed when imported.

---
