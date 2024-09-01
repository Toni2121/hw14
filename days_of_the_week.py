def day_of_the_week(num: int):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    if num in days:
        return days[num]
    else:
        raise ValueError("Number must be between 1 and 7")