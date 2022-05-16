def area_of_triangle(opposite, base, hypotenuse):
    area = 1/2 * (float(base) * float(hypotenuse))
    return area


try:
    checkArea = area_of_triangle(2.5, 3, 5)
    #   print(f"Area is: {checkArea}")

except (ValueError, NameError):
    print("Maybe try with a different value (-_0)")

