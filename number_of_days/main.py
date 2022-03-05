def number_of_days(year,month):
    """
    Write a function that returns the number of calendar days in a given year and month.

    :param year: A number(int)
    :param month: A number(int) from 1 to 12
    :return: A number(int)
    """
    assert isinstance(year, int)
    assert isinstance(month, int)
    assert year > 0
    assert month >= 1
    assert month <= 12

    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    day = days[month - 1]
    if month == 2:
        if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            day += 1
    return day


def number_of_leap_years(year1,year2):
    """
    Write a function to find the number of leap-years between (including both endpoints) two given years.

    :param year1: A number(int)
    :param year2: A number(int)
    :return: A number(int)
    """
    assert isinstance(year1, int)
    assert isinstance(year2, int)
    assert year1 <= year2

    begin4 = (year1 - 1) // 4
    begin100 = (year1 - 1) // 100
    begin400 = (year1 - 1) // 400
    left = begin4 - begin100 + begin400

    end4 = year2 // 4
    end100 = year2 // 100
    end400 = year2 // 400
    right = end4 - end100 + end400

    result = right - left
    return result

# print(number_of_leap_years(2021, 2022))

def get_day_of_week(year,month,day):
    """
    Write a function to find the string name (e.g., Monday, Tuesday)
    of the day of the week on a given month,day, and year.

    :param year: A number(int)
    :param month: A number(int) from 1 to 12
    :param day: A number(int)
    :return: A number(int)
    """
    assert isinstance(year, int)
    assert isinstance(month, int)
    assert isinstance(day, int)
    assert year > 0
    assert month >= 1
    assert month <= 12
    assert day >= 1
    assert day <= 31

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if month == 1 or month == 2:
        month += 12
        year -= 1
    week = (day + 2 * month + 3 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400 + 1) % 7
    return days[week]


# print(get_day_of_week(2022,1,21))
