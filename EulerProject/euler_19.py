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
    while DATE['day'] != 31 and DATE['month'] != 11 and DATE['year'] != 2000:
        print(DATE)
        if DATE['year'] % 4 == 0:
            MONTHS[1] = 29
        else:
            MONTHS[1] = 28
        if DATE['weekday'] == 0 and DATE['day'] == 1:
            total += 1
        DATE['day'] += 1
        DATE['weekday'] += 1
        if DATE['weekday'] > 6:
            DATE['weekday'] = 0
        if DATE['day'] > MONTHS[DATE['month']]:
            DATE['day'] = 1
            DATE['month'] += 1
        if DATE['month'] > len(MONTHS):
            DATE['month'] = 0
            DATE['year'] += 1
    return total