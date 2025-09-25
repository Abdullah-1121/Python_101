# Identity vs Equality
a = [1, 2]
b = [1, 2]
print(a == b)  # True → values are equal
print(a is b)  # False → different objects in memory



# Short-circuiting
x = 0
y = 10
if x != 0 and (y / x) > 1:
    print("yes")
else:
  print("no")


# Won’t raise ZeroDivisionError because x != 0 is False, so Python skips the second part.


#  INDEXING
s = "python"
s[0] # p   starts from first letter
s[-1] # n  - starts from the last letter

#  SLICING
print(s[1:4]) # yth
print(s[2:]) # thon
print(s[:3]) # pyt
print(s[::-1]) # Reverses the string : nohtyp
print(r"C:\Users\Name")  # prints as is

# s[start : stop : step]
s = "abcdef"
print(s[1:5:2]) #bd
# Start at index 1 → 'b'
# Stop before index 5 → indices [1,2,3,4]
# Step 2 → take every 2nd element → 'b' (index 1), 'd' (index 3)

s = "abcdef"
print(s[::2])  # take every 2nd character → 'ace'
print(s[::-1]) # reverse string → 'fedcba'


# Useful string methods
s = "  hello world  "
print(s.strip())        # "hello world" → removes leading/trailing spaces
print(s.replace(" ", "_"))  # "__hello_world__"
print(s.replace("o" , "O")) #  hellO wOrld

# 📌 Day 3 Cheat Sheet – Operators & Strings
# 1️⃣ Operator Precedence (Top to Bottom)
# Precedence	Operator Type	Example
# 1	** (exponent)	2 ** 3
# 2	+x, -x, ~x (unary)	-5
# 3	*, /, //, %	3*4, 7//3
# 4	+, -	2+3-1
# 5	<<, >> (bit shift)	2<<1
# 6	& (bitwise AND)	6 & 3
# 7	^ (bitwise XOR)	6 ^ 3
# 8	`	` (bitwise OR)
# 9	==, !=, >, <, >=, <=	2 == 2
# 10	is, is not, in, not in	[1] is [1]
# 11	not	not True
# 12	and	True and False
# 13	or	True or False

# 💡 Tip: Memorize as *“Exponent → Unary → /% → +- → Shifts → Bitwise → Comparisons → Identity → not → and → or”

# 2️⃣ Identity vs Equality
# a = [1,2]; b = [1,2]; c = a
# a == b  # True (values)
# a is b  # False (different objects)
# a is c  # True (same object)

# 3️⃣ Short-Circuiting

# and → stops if first False

# or → stops if first True

# x = 0; y = 10
# x != 0 and (y / x) > 1  # False, no ZeroDivisionError

# 4️⃣ Floor Division //

# Rounds down to nearest integer

# 7 // 3 = 2
# -7 // 3 = -3

# 5️⃣ Bitwise Operators
# Operator	Example	Explanation
# &	6 & 3	010 & 011 → 010 → 2
# 		6
# ^	6 ^ 3	XOR → 010 ^ 011 → 001 → 1
# ~	~6	bitwise NOT → -7
# 6️⃣ String Indexing & Slicing

# Indexing:

# s = "Python"
# s[0] = 'P'  # char at index 0
# s[-1] = 'n' # last char


# Slicing: s[start:stop:step]

# start → inclusive, stop → exclusive, step → jump

# s = "abcdef"
# s[1:5:2]  # 'bd'
# s[::-1]   # reverse → 'fedcba'


# Useful methods:

# s.strip()       # remove leading/trailing spaces
# s.replace(" ", "_")  # replace
# r"C:\path"      # raw string, ignore \ escape

# 7️⃣ Exam Tips

# Step digit by digit for slicing.

# Remember stop index is exclusive.

# Negative step → reverse direction.

# Floor division → always floor, watch negative numbers.

# Identity vs equality often confuses students → is = same object, == values equal.