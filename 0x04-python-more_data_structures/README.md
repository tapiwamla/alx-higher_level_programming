# Tasks

## 0. Squared Simple

**Prototype:** `def square_matrix_simple(matrix=[]):`

Write a function that computes the square value of all integers of a matrix.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
```

Output:
```
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## 1. Search and Replace

**Prototype:** `def search_replace(my_list, search, replace):`

Write a function that replaces all occurrences of an element by another in a new list.

```python
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
```

Output:
```
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
```

## 2. Unique Addition

**Prototype:** `def uniq_add(my_list=[]):`

Write a function that adds all unique integers in a list (only once for each integer).

```python
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
```

Output:
```
Result: 15
```

## 3. Present in Both

**Prototype:** `def common_elements(set_1, set_2):`

Write a function that returns a set of common elements in two sets.

```python
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
```

Output:
```
['C']
```

## 4. Only Differents

**Prototype:** `def only_diff_elements(set_1, set_2):`

Write a function that returns a set of all elements present in only one set.

```python
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
```

Output:
```
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
```

## 5. Number of Keys

**Prototype:** `def number_keys(a_dictionary):`

Write a function that returns the number of keys in a dictionary.

```python
a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
```

Output:
```
Number of keys: 3
```

## 6. Print Sorted Dictionary

**Prototype:** `def print_sorted_dictionary(a_dictionary):`

Write a function that prints a dictionary by ordered keys.

```python
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
```

Output:
```
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
```

## 7. Update Dictionary

**Prototype:** `def update_dictionary(a_dictionary, key, value):`

Write a function that replaces or adds key/value in a dictionary.

```python
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
```

Output:
```
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
```

## 8. Simple Delete by Key

**Prototype:** `def simple_delete(a_dictionary, key=""):`

Write a function that deletes a key in a dictionary.

```python
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
```

Output:
```
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
```

## 9. Multiply by 2

**Prototype:** `def multiply_by_2(a_dictionary):`

Write a function that returns a new dictionary with all values multiplied by 2.

```python
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
```

Output:
```
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
```

## 10. Best Score

**Prototype:** `def best_score(a_dictionary):`

Write a function that returns a key with the biggest integer value.

```python
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)


print("Best score: {}".format(best_key))
```

Output:
```
Best score: Molly
Best score: None
```

## 11. Multiply by Using Map

**Prototype:** `def multiply_list_map(my_list=[], number=0):`

Write a function that returns a list with all values multiplied by a number without using any loops.

```python
my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)
```

Expected Output:
```
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
```

## 12. Roman to Integer

**Prototype:** `def roman_to_int(roman_string):`

Create a function `def roman_to_int(roman_string):` that converts a Roman numeral to an integer. You can assume the number will be between 1 to 3999.

```python
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
```

Output:
```
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
```
