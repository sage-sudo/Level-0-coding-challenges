def time_conversion(num):
    number = int(num)

    handlesPlurasForHours = "hour"
    handlesPlurasForMinuets = "minuet"

    count_hours = 0

    while number >= 60:
        number -= 60
        count_hours += 1

    take_minuets = number

    if count_hours > 1:
        handlesPlurasForHours = "hours"

    if take_minuets > 1:
        handlesPlurasForMinuets = "minuets"

    time = f"{count_hours} {handlesPlurasForHours}, {take_minuets} {handlesPlurasForMinuets}."
    #   print(time)
    return time


timed = time_conversion(133)

print(timed)
