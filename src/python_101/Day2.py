#  Mutable and Immutable data types

#  Mutable : Elements can be changed such as List
list1 = [1 , 2 , 3]
list1[1] = 3
print(list1) # [1 , 3 , 3]

# Immutable : can't change individual characters

#  Strings
s = "hello"
# s[1]= "H" ----> Invalid Operation

#  Tuples
t = (1 , 2 , 3)
# t(1) = 2  -----> Invalid operation

#  But if it contains an immutable such as a list in the tuple than we can change it indiidually
t = (1 , [2,3])
t[1].append(4)   # (1, [2, 3, 4])
print(t)


# Sets
# Mutable, but elements must be immutable (so no lists inside a set).
# Dictionaries
# Keys must be immutable (string, number, tuple), values can be anything.

# isinstance()

# Check type of an object:

x = [1, 2, 3]
print(isinstance(x, list))  # True
print(isinstance(x, tuple)) # False


# Flashcard 1: Strings

# Q: Can you change a character in a string?
# A: ❌ No, strings are immutable. You can only create a new string.

# Flashcard 2: Tuples

# Q: Are tuples mutable?
# A: Mostly ❌ No. But if a tuple contains a mutable object (like a list), that object can be changed.

# Flashcard 3: Lists

# Q: Can you modify, add, or remove elements in a list?
# A: ✅ Yes, lists are mutable.

# Flashcard 4: Sets

# Q: Are sets mutable? Can they contain mutable objects?
# A: ✅ Sets themselves are mutable (add/remove items).
# ❌ Elements must be immutable.

# Flashcard 5: Dictionaries

# Q: Which part of a dict is immutable?
# A: Keys must be immutable.
# Values can be anything (mutable or immutable).

# Flashcard 6: Boolean Evaluation

# Q: Which of these are False? 0, [], [0], "", "False", None
# A: 0, [], "", None → False
# [0], "False" → True

# ✅ Quick Tip for Exams:

# Immutable: strings, tuples, numbers, frozensets

# Mutable: lists, dicts, sets

# Shallow immutability: immutable container can hold mutable objects