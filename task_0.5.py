import math

# Formula for parameter : s = 1/2 (a+b+c)
# Formula for Area : A = square_root(s (s - a) (s - b) (s - c))


def triangle_area_by_sides(opposite, base, hypotenuse):
    opposite = float(opposite)
    base = float(base)
    hypotenuse = float(hypotenuse)

    parameter = 1/2 * (opposite + base + hypotenuse)

    are_of_triangle = math.sqrt(parameter * ((parameter - opposite) * (parameter - base) * (parameter - hypotenuse)))
    
    return are_of_triangle

    

try:
    checkArea = triangle_area_by_sides(3, 4, 5)
    print(f"Area is: {checkArea}")

except (ValueError, NameError):
    print("Maybe try with a different value (-_0)")

