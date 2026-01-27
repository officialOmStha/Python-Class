# Sum of real and imaginary parts of two complex number.

# Input two complex numbers
z1 = complex(input("Enter first complex number: "))
z2 = complex(input("Enter second complex number: "))

# Sum of the two complex numbers
result = z1 + z2

# Display real and imaginary parts
print("Sum of real parts:", result.real)
print("Sum of imaginary parts:", result.imag)
print("Resulting complex number:", result)
