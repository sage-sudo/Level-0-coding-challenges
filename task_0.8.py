def time_convertion(num):
    number = int(num)

    handles_pluras_for_hours = "hour"
    handles_pluras_for_minuets = "minuet"

    count_hours = 0

    while number >= 60:
        number -= 60
        count_hours += 1

    take_minuets = number

    if count_hours > 1 or count_hours == 0:
        handles_pluras_for_hours = "hours" 

    if take_minuets > 1 or take_minuets == 0:
        handles_pluras_for_minuets = "minuets"

    time = f"{count_hours} {handles_pluras_for_hours}, {take_minuets} {handles_pluras_for_minuets}."
    #   print(time)
    return time


timed = time_convertion(133)

print(timed)
