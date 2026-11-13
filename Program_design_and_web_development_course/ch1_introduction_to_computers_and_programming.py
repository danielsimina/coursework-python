# CTST 1305 - Chapter 1: Introduction to Computers and Programming
# Run this script in IDLE, VS Code, or any Python 3 interpreter.

# 1. Displaying Output (The print function)
print("Welcome to CTST 1305: Programming Design & Web Development!")
print("-" * 55)

# 2. How Computers Store Characters (ASCII/Unicode & Binary)
letter = "A"
ascii_code = ord(letter)       # Converts character to its numeric code
binary_value = bin(ascii_code) # Converts number to binary (0s and 1s)

print(f"Character: '{letter}'")
print(f"Numeric ASCII Code: {ascii_code}")
print(f"Stored in Memory (Binary): {binary_value}")
print("-" * 55)

# 3. Basic Input, Processing, and Output (IPO Model)
user_name = input("Enter your name: ")
birth_year = int(input("Enter your birth year (e.g., 2005): "))

# Processing data in the CPU
current_year = 2026
estimated_age = current_year - birth_year

# Outputting the result
print(f"\nHello, {user_name}! In {current_year}, you turn {estimated_age} years old.")