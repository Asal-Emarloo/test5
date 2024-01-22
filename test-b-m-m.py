def b_m_m(x, y):
    while(y):
    x, y = y, x % y
    return x

num1 = int(input("Enter first number:   " ))
num2 = int(input("Enter second number:  "))

print("b.m.m numbers:   ", b_m_m(num1, num2))