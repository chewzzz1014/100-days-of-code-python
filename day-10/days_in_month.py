def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year&400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year=2022, month=2):
    if not is_leap_year(year) and month==2:
        return 28
    elif  is_leap_year(year) and month ==2:
        return 29
    else:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        else:
            return 30


print(days_in_month())