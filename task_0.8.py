def time_convertion(num):
    number = int(num)

    handles_pluras_for_hours = "hour"
    handles_pluras_for_minutes = "minute"

    count_hours = 0

    while number >= 60:
        number -= 60
        count_hours += 1

    take_minutes = number

    if count_hours > 1 or count_hours == 0:
        handles_pluras_for_hours = "hours" 

    if take_minutes > 1 or take_minutes == 0:
        handles_pluras_for_minutes = "minutes"

    time = f"{count_hours} {handles_pluras_for_hours}, {take_minutes} {handles_pluras_for_minutes}."
  
    return time


timed = time_convertion(133)

print(timed)
