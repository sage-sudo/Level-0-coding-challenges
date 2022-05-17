def maximum(x, y, z):
    x_number = float(x)
    y_number = float(y)
    z_number = float(z)

    store_numbers = [x, y, z]

    max_value = store_numbers[0]
    for number in store_numbers:
        if number > max_value:
            max_value = number

    return max_value


try:
    the_maximum = maximum(1, 22, 3.2)
    print("The Bigger number is:", the_maximum)

except (ValueError, NameError):
    print("You really should check your arguments (-,-\")")
