# Activity 5: Taking Input and Type Casting in Python

# Taking input as string
name = input("Enter your name:")
print("hello",name)

# Taking integer input (by default input() gives string)
age = int(input("Enter your age:"))
print("You are", age, "years old.")

# Taking two numbers and adding them
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

sum_value = num1 + num2
print("sum =", sum_value)

# Taking float input
height = float(input("Enter your height in meters:"))
print("Your height is:", height,"meters")