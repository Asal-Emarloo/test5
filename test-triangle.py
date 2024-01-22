def triangle(side1, side2, side3):
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        return True
    else:
        return False

side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

if triangle(side1, side2, side3):
    print("It is possible to form a triangle with these side lengths. :triangular_ruler:")
else:
    print("It is not possible to form a triangle with these side lengths. :x:")def triangle(side1, side2, side3):
     if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        return True
     else:
        return False

side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

if triangle(side1, side2, side3):
    print("It is possible to form a triangle with these side lengths. :triangular_ruler:")
else:
    print("It is not possible to form a triangle with these side lengths. :x:")



