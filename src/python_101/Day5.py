# IF Else and control structures
x = int(input("Enter a number: "))
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# In Python, a for or while loop can have an else clause. The else part runs only if the loop completes without hitting a break.

# Example:

for n in range(2, 6):
    if n % 2 == 0:
        print(f"{n} is even")
        break
else:
    print("No even numbers found")


l1  = [1  , 3 , 5 , 9]
for l in l1:
    if l == 7 :
        print("Found 7")
        break
else:
    print("7 not found")



#  Try Except
denominator = int(input("Enter denominator: "))
try:
    result = 10 / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Walrus operator (:=)
# Introduced in Python 3.8.

# Assigns a value to a variable as part of an expression.

# Helps avoid repeating expressions.

# Example 1: In a loop
words = ["apple", "banana", "cherry"]
while (n := len(words)) > 0:
    print("Number of words:", n)
    words.pop()


#  GENERATOR FUNCTIONS
def even_numbers():
    for num in range(10):
        if num % 2 == 0:
            yield num

for even in even_numbers():
    print(even)