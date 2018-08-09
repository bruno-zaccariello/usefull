# 1 Jan. 1900 = Monday
# Calculate the total of sundays on first of the month
# between Y:1900 and Y:2000

MONTHS = [31,28,31,30,31,30,31,31,30,31,30,31]
WEEKDAY = [0,1,2,3,4,5,6] # 0 = Sunday
YEAR = 365

def get_result():
    # DATE = (DAY, MONTH, YEAR, WEEKDAY)
    DATE = {'day':1,
            'month':0,
            'year':1900,
            'weekday':1}
    total = 0
    while True:
        # If hits 31 Dec. 2000 it stops
        if DATE['day'] == 31 and DATE['month'] == 11 and DATE['year'] == 2000:
            break

        # Tests for leap years
        if DATE['year'] % 4 == 0 and not str(DATE['year']).endswith('00'):
            MONTHS[1] = 29
        elif DATE['year'] % 400 == 0 and str(DATE['year']).endswith('00'):
            MONTHS[1] = 29
        else:
            MONTHS[1] = 28

        # If it is a Sunday on First of the Month it counts
        if DATE['weekday'] == 0 and DATE['day'] == 1 and DATE['year'] > 1900:
            total += 1

        # Adds day and weekday
        DATE['day'] += 1
        DATE['weekday'] += 1

        # Fix weekdays
        if DATE['weekday'] > 6:
            DATE['weekday'] = 0

        # Add months if day exceeds that month total
        if DATE['day'] > MONTHS[DATE['month']]:
            DATE['day'] = 1
            DATE['month'] += 1

        # Add Year if month exceeds dec.
        if DATE['month'] >= len(MONTHS):
            DATE['month'] = 0
            DATE['year'] += 1
    return total