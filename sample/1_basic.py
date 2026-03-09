#!/usr/bin/env python3

try:
    x = int(input("Input? "))
    print(10 / x)

except ZeroDivisionError:
    print("Division by zero!")

except ValueError:
    print("Invalid input")
