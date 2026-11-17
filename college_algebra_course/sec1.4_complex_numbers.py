# MATH 1111 Section 1.4: Complex Numbers in Python
# Note: Python uses 'j' for the imaginary unit (e.g., 3 + 2j)

z1 = 3 + 2j
z2 = 1 - 4j

print("--- Complex Numbers ---")
print(f"z1 = {z1}")
print(f"z2 = {z2}\n")

# 1. Addition
print("Addition (z1 + z2):", z1 + z2)

# 2. Subtraction
print("Subtraction (z1 - z2):", z1 - z2)

# 3. Multiplication
print("Multiplication (z1 * z2):", z1 * z2)

# 4. Division
print("Division (z1 / z2):", z1 / z2)

# 5. Complex Conjugate
print("Conjugate of z1:", z1.conjugate())
print("Conjugate of z2:", z2.conjugate())

# 6. Powers of i cycle demonstration
print("\n--- Powers of i ---")
for n in range(9):
    val = 1j**n
    print(f"i^{n} = {val.real:2.0f} + {val.imag:2.0f}j")