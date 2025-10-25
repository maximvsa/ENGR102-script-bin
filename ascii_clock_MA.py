# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Maximus Amick
#               Daniel Yoo
#               Caleb Carter
#               Noah Kim
# Section:      513
# Assignment:   8.17 LAB: ASCII clock
# Date:         22 October 2025

def format_display_time(hours, minutes, clock_type):
    # Handle midnight (00:00) in 12-hour format
    if int(hours) == 0 and clock_type == "12":
        display_time = f"1 2 : {minutes[0]} {minutes[1]} A M"
    # Handle single-digit AM hours (1-9) in 12-hour format
    elif int(hours) < 10 and clock_type == "12":
        display_time = f"{hours[1]} : {minutes[0]} {minutes[1]} A M"
    # Handle double-digit AM hours (10-11) in 12-hour format
    elif 12 > int(hours) >= 10 and clock_type == "12":
        display_time = f"{hours[0]} {hours[1]} : {minutes[0]} {minutes[1]} A M"
    # Handle noon (12:00) in 12-hour format
    elif int(hours) == 12 and clock_type == "12":
        display_time = f"1 2 : {minutes[0]} {minutes[1]} P M"
    # Handle single-digit PM hours (13-21) in 12-hour format
    elif 22 > int(hours) > 12 and clock_type == "12":
        display_time = f"{int(hours) - 12} : {minutes[0]} {minutes[1]} P M"
    # Handle double-digit PM hours (22-23) in 12-hour format
    elif int(hours) > 22 and clock_type == "12":
        display_time = f"{' '.join(str(int(hours) - 12))} : {minutes[0]} {minutes[1]} P M"
    # Handle midnight (00:00) in 24-hour format
    elif int(hours) == 0 and clock_type == "24":
        display_time = f"0 : {minutes[0]} {minutes[1]}"
    # Handle single-digit hours (0-9) in 24-hour format
    elif int(hours) < 10 and clock_type == "24":
        display_time = f"0 {hours[1]} : {minutes[0]} {minutes[1]}"
    # Handle double-digit hours (10-23) in 24-hour format
    elif int(hours) >= 10 and clock_type == "24":
        display_time = f"{hours[0]} {hours[1]} : {minutes[0]} {minutes[1]}"
    return display_time
