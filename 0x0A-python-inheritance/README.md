### Task 0: Lookup

**Description:** Write a function that returns the list of available attributes and methods of an object.

```python
def lookup(obj):
    # Your code here
```

### Task 1: My List

**Description:** Write a class `MyList` that inherits from `list` with a public instance method `print_sorted` that prints the list in ascending order.

```python
class MyList(list):
    def print_sorted(self):
        # Your code here
```

### Task 2: Exact Same Class

**Description:** Write a function that returns `True` if the object is exactly an instance of the specified class; otherwise, it returns `False`.

```python
def is_same_class(obj, a_class):
    # Your code here
```

### Task 3: Same Class or Inherit From

**Description:** Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise, it returns `False`.

```python
def is_kind_of_class(obj, a_class):
    # Your code here
```

### Task 4: Only Subclass of

**Description:** Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise, it returns `False`.

```python
def inherits_from(obj, a_class):
    # Your code here
```

### Task 5: Geometry Module

**Description:** Write an empty class `BaseGeometry`.

```python
class BaseGeometry:
    # Your code here
```

### Task 6: Improve Geometry

**Description:** Write a class `BaseGeometry` with a public instance method `area` that raises an Exception with the message "area() is not implemented."

```python
class BaseGeometry:
    def area(self):
        # Your code here
```

### Task 7: Integer Validator

**Description:** Write a class `BaseGeometry` with a public instance method `integer_validator` that validates an integer value.

```python
class BaseGeometry:
    def integer_validator(self, name, value):
        # Your code here
```

### Task 8: Rectangle

**Description:** Write a class `Rectangle` that inherits from `BaseGeometry` with instantiation for width and height.

```python
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        # Your code here
```

### Task 9: Full Rectangle

**Description:** Write a class `Rectangle` that inherits from `BaseGeometry` with instantiation for width and height and an implemented `area` method.

```python
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        # Your code here
```

### Task 10: Square #1

**Description:** Write a class `Square` that inherits from `Rectangle` with instantiation for size.

```python
class Square(Rectangle):
    def __init__(self, size):
        # Your code here
```

### Task 11: Square #2

**Description:** Write a class `Square` that inherits from `Rectangle` with instantiation for size and an implemented `area` method.

```python
class Square(Rectangle):
    def __init__(self, size):
        # Your code here
```

