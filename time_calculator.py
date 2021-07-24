def add_time(start, duration, day=None):

    days = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    periods = {
        'AM': 'PM',
        'PM': 'AM'
    }

    old_hr = int(start.split()[0].split(':')[0])
    old_mn = int(start.split()[0].split(':')[1])
    period =  start.split()[1]
    
    new_hr = int(duration.split(':')[0])
    new_mn = int(duration.split(':')[1])
    n_days = int(new_hr / 24)

    mn = old_mn + new_mn

    if mn >= 60:
        old_hr += 1
        mn %= 60

    p_cyle = int((old_hr + new_hr) / 12)

    hr = (old_hr + new_hr) % 12

    if mn < 10:
        mn = '0' + str(mn)

    if hr == 0:
        hr = 12

    if period == 'PM' and old_hr + (new_hr % 12) >= 12:
        n_days += 1
    
    if p_cyle % 2 == 1:
        period = periods[period]

    new_time = f'{hr}:{mn} {period}'

    if day:
        index = int((days[day.lower()] + n_days) % 7)
        day = list(days.keys())[list(days.values()).index(int(index))]
        new_time += ', ' + day.capitalize()
    
    if n_days == 1:
        return f'{new_time} (next day)'
    elif n_days > 1:
        return f'{new_time} ({n_days} days later)'

    return new_time
