import sys

n1 = float(sys.argv[1])
n2 = float(sys.argv[2])

print("Addition:", n1 + n2)
print("Subtraction:", n1 - n2)
print("Multiplication:", n1 * n2)

if n2 != 0:
    print("Division:", n1 / n2)
else:
    print("Cannot divide by zero")
