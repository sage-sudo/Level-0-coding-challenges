def triangle_area_by_sides(side1, side2, side3):
    side1 = float(side1)
    side2 = float(side2)
    side3 = float(side3)

    parameter = 1 / 2 * (side1 + side2 + side3)

    are_of_triangle = (parameter * ((parameter - side1) * (parameter - side2) * (parameter - side3))) ** (1/2)
    
    return are_of_triangle


try:
    checkArea = triangle_area_by_sides(3, 4, 5)
    print(f"Area is: {checkArea}")

except (ValueError, NameError):
    print("Maybe try with a different value (-_0)")

