#  Lists
#  Ordered, Mutable, Allows Duplicates
list1 = [1, 2, 3, 4, 5]
list2 = ["apple", "banana", "cherry"]
list3 = [1, "apple", 3.14, True]

#  Reference behavior
a = [1, 2, 3]
b = a
b.append(4) # a is now [1, 2, 3, 4] because lists are mutable and b references the same list as a
print(a) # [1, 2, 3, 4]


#  Make a separate copy of a list
c = a[:] # or c = list(a)
c.append(5) # a is still [1, 2, 3, 4]
print(a) # [1, 2, 3, 4]
print(c) # [1, 2, 3, 4, 5]


#  SLICING
#  list[start:stop:step]
sublist = list1[1:4] # [2, 3, 4]
print(sublist) # [2, 3, 4]
reverse_list = list1[::-1] # [5, 4, 3, 2, 1]


#  Unpacking
x, y, z = [1, 2, 3] # x=1, y=2, z=3


# 2️⃣ Tuples

# Definition:

# Ordered, immutable collection of items.

# Use parentheses () (or just commas) to define.

# Can hold different types, including nested lists (mutable objects).

t1 = (1, 2, 3)
t2 = 1, 2, 3        # parentheses optional
t3 = (1, [2, 3], 4) # inner list is mutable

# A. Immutability
t = (1, 2, 3)
t[0] = 99  # ❌ Error: tuples cannot be changed

# B. Quirks

# Single element tuple must have a comma:

t = (1,)   # ✅ single element
t = (1)    # ❌ this is just an int


# Tuples can contain mutable objects:

t = (1, [2,3])
t[1].append(4)
print(t)  # (1, [2, 3, 4]) ✅ inner list changed




# 3️⃣ Sets

# Definition:

# Unordered collection of unique elements.

# Mutable, but no duplicates.

s = {1, 2, 3, 3}
print(s)  # {1, 2, 3}

# A. Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union → {1, 2, 3, 4, 5}
print(a & b)  # Intersection → {3}
print(a - b)  # Difference → {1, 2}

# B. frozenset

# Immutable set

fs = frozenset([1, 2, 3])
# fs.add(4) ❌ Error



# 4️⃣ Dictionaries

# Definition:

# Collection of key → value pairs.

# Keys must be immutable (numbers, strings, tuples)

# Values can be any type.

d = {"name": "Alice", "age": 25}

# A. Overwriting Keys
d = {"a": 1, "a": 2}
print(d)  # {"a": 2} → last value wins

# B. Dictionary Comprehensions
squares = {x: x**2 for x in range(5)}
print(squares)  # {0:0, 1:1, 2:4, 3:9, 4:16}

# With condition
even_squares = {x: x**2 for x in range(5) if x%2==0}
print(even_squares)  # {0:0, 2:4, 4:16}

# C. Length
d = {"a": 1, "b": 2}
print(len(d))  # 2