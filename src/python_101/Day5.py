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