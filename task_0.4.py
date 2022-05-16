def even_or_odd(number):
    try:
        number = int(number)

        if number % 2 == 0:
            print("even")

        else:
            print("odd")

    except ValueError:
        print("Enter a proper integer value")


even_or_odd(3)
# even_or_odd("Sting not accepted")
