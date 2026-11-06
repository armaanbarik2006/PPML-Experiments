"""
Swap two integers using bitwise XOR

Python lab experiment.
Run: python 08_swap_using_bitwise_xor.py
"""
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("a =", a)
print("b =", b)
