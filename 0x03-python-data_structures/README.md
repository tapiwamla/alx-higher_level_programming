# Tasks

## Task 0: Print a list of integers (mandatory)
Write a function that prints all integers of a list.

**Prototype:** `def print_list_integer(my_list=[]):`

**Format:** one integer per line. See example

**You are not allowed to import any module**

**You can assume that the list only contains integers**

**You are not allowed to cast integers into strings**

**You have to use `str.format()` to print integers**

```python
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$
```

**Repo:**

GitHub repository: [alx-higher_level_programming](https://github.com/alx-higher_level_programming)

Directory: 0x03-python-data_structures

File: 0-print_list_integer.py

## Task 1: Secure access to an element in a list (mandatory)
Write a function that retrieves an element from a list like in C.

**Prototype:** `def element_at(my_list, idx):`

**If idx is negative, the function should return None**

**If idx is out of range (> of number of elements in my_list), the function should return None**

**You are not allowed to import any module**

**You are not allowed to use try/except**

```python
guillaume@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$
```

**Repo:**

GitHub repository: [alx-higher_level_programming](https://github.com/alx-higher_level_programming)

Directory: 0x03-python-data_structures

File: 1-element_at.py

## Task 2: Replace element (mandatory)
Write a function that replaces an element of a list at a specific position (like in C).

**Prototype:** `def replace_in_list(my_list, idx, element):`

**If idx is negative, the function should not modify anything, and returns the original list**

**If idx is out of range (> of number of elements in my_list), the function should not modify anything, and returns the original list**

**You are not allowed to import any module**

**You are not allowed to use try/except**

```python
guillaume@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$
```

**Repo:**

GitHub repository: [alx-higher_level_programming](https://github.com/alx-higher_level_programming)

Directory: 0x03-python-data_structures

File: 2-replace_in_list.py

## Task 3: Print a list of integers... in reverse! (mandatory)
Write a function that prints all integers of a list, in reverse order.

**Prototype:** `def print_reversed_list_integer(my_list=[]):`

**Format:** one integer per line. See example

**You are not allowed to import any module**

**You can assume that the list only contains integers**

**You are not allowed to cast integers into strings**

**You have to use `str.format()` to print integers**

```python
guillaume@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$
```

**Repo:**

GitHub repository: [alx-higher_level_programming](https://github.com/alx-higher_level_programming)

Directory: 0x03-python-data_structures

File: 3-print_reversed_list_integer.py

## Task 4: Replace in a copy (mandatory)
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

**Prototype:** `def new_in_list(my_list, idx, element):`

**If idx is negative, the function should return a copy of the original list**

**If idx is out of range (> of number of elements in my_list), the function should return a copy of the original list**

**You are not allowed to import any module**

**You are not allowed to use try/except**

```python
guillaume@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$
```

**Repo:**

GitHub repository: [alx-higher_level_programming](https://github.com/alx-higher_level_programming)

Directory: 0x03-python-data_structures

File: 4-new_in_list.py

## Task 5: Can you C me now? (mandatory)
Write a function that removes all characters 'c' and 'C' from a string.

**Prototype:** `def no_c(my_string):`

**The function should return the new string**

**You are not allowed to import any module**

**You are not allowed to use str.replace()**

```python
guillaume@ubuntu:~/0x03$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

gu

illaume@ubuntu:~/0x03$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$
```

**Repo:**

GitHub repository: [alx-higher_level_programming](https://github.com/alx-higher_level_programming)

Directory: 0x03-python-data_structures

File: 5-no_c.py

## Task 6: Lists of lists = Matrix (mandatory)
Write a function that prints a matrix of integers.

**Prototype:** `def print_matrix_integer(matrix=[[]]):`

**Format:** see example

**You are not allowed to import any module**

**You can assume that the list only contains integers**

**You are not allowed to cast integers into strings**

**You have to use `str.format()` to print integers**

```python
guillaume@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$
```

**Repo:**

GitHub repository: [alx-higher_level_programming](https://github.com/alx-higher_level_programming)

Directory: 0x03-python-data_structures

File: 6-print_matrix_integer.py

## Task 7: Tuples addition (mandatory)
Write a function that adds 2 tuples.

**Prototype:** `def add_tuple(tuple_a=(), tuple_b=()):`

**Returns a tuple with 2 integers:**

- The first element should be the addition of the first element of each argument
- The second element should be the addition of the second element of each argument

**You are not allowed to import any module**

**You can assume that the two tuples will only contain integers**

**If a tuple is smaller than 2, use the value 0 for each missing integer**

**If a tuple is bigger than 2, use only the first 2 integers**

```python
guillaume@ubuntu:~/0x03$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/0x03$
```

**Repo:**

GitHub repository: [alx-higher_level_programming](https://github.com/alx-higher_level_programming)

Directory: 0x03-python-data_structures

File: 7-add_tuple.py

## Task 8: More returns! (mandatory)
Write a function that returns a tuple with the length of a string and its first character.

**Prototype:** `def multiple_returns(sentence):`

**If the sentence is empty, the first character should be equal to None**

**You are not allowed to import any module**

```python
guillaume@ubuntu:~/0x03$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/0x03$ ./8-main.py
Length: 22 - First character: A
guillaume@ubuntu:~/0x03$
```

**Repo:**

GitHub repository: [alx-higher_level_programming](https://github.com/alx-higher_level_programming)

Directory: 0x03-python-data_structures

File: 8-multiple_returns.py

## Task 9: Find the max (mandatory)
Write a function that finds the biggest integer of a list.

**Prototype:** `def max_integer(my_list=[]):`

**If the list is empty, return None**

**You can assume that the list only contains integers**

**You are not allowed to import any module**

**You are not allowed to use the builtin max()**

```python
guillaume@ubuntu:~/0x03$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

guillaume@ubuntu:~/0x03$ ./9-main.py
Max: 90
guillaume@ubuntu:~/0x03$
```

**Repo:**

GitHub repository: [alx-higher_level_programming](https://github.com/alx-higher_level_programming)

Directory: 0x03-python-data_structures

File: 9-max_integer.py

## Task 10: Only by 2 (mandatory)
Write a function that finds all multiples of 2 in a list.

**Prototype:** `def divisible_by_2(my_list=[]):`

**Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2**

**The new list should have the same size as the original list**

**You are not allowed to import any module**

```python
guillaume@ubuntu:~/0x03$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

guillaume@ubuntu:~/0x03$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/0x03$
```

**Repo:**

GitHub repository: [alx-higher_level_programming](https://github.com/alx-higher_level_programming)

Directory: 0x03-python_data_structures

File: 10-divisible_by_2.py

## Task 11: Delete at (mandatory)
Write a function that deletes the item at a specific position in a list.

**Prototype:** `def delete_at(my_list=[], idx=0):

`

**If idx is negative or out of range, nothing changes (returns the same list)**

**You are not allowed to use pop()**

**You are not allowed to import any module**

```python
guillaume@ubuntu:~/0x03$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/0x03$
```

**Repo:**

GitHub repository: [alx-higher_level_programming](https://github.com/alx-higher_level_programming)

Directory: 0x03-python_data_structures

File: 11-delete_at.py
```
