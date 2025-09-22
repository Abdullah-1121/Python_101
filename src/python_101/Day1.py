#  TYPE ANNOTATIONS

# Type hints don’t enforce types → Python will only complain if the operation itself is invalid at runtime.

def product(a: int, b: int) -> int:
    return a * b


print(product(2, 3))  # 6 -> valid operation 
print(product("a", 3))  # valid operation -> 'aaa' ( Because str can be multiplied by int)
# print(product('2', '3'))  # invalid operation -> TypeError at runtime ( Because str can't be multiplied by str)



#  INPUT METHOD 
#  input() function always returns a string.
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello, {name}. You are {age} years old.")
print(type(name))  # <class 'str'>
print(type(age))   # <class 'str'> , we need to convert it to int if we want to perform arithmetic operations.
age = int(age)  # converting age to int


# Python = “write once, run anywhere” (as long as Python interpreter is present).

# .pyc files = cached bytecode for faster execution.