def add_time(start_time, new_time, day=None):

    days = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    old_hour = int(start_time.split(':')[0])
    old_minute = int(start_time.split(':')[1].split()[0])
    old_period = start_time.split()[-1]

    new_hour = int(new_time.split(':')[0])
    new_minute = int(new_time.split(':')[1])

    period = None
    n_days = 0

    if old_hour == 12 and old_period == 'AM':
        old_hour = 0

    elif old_hour == 12 and old_period == 'PM':
        pass

    elif old_hour >= 1 and old_period == 'PM':
        old_hour += 12

    hour = old_hour + new_hour
    minute = old_minute + new_minute

    if minute >= 60:
        hour += 1
        minute %= 60

    if hour >= 24:
        n_days = int(hour / 24)
        hour %= 24

    if minute < 10:
        minute = f'0{minute}'

    if not hour:
        hour = 12
        period = 'AM'

    if hour < 12:
        period = 'AM'
 
    elif hour == 12 and not period:
        hour = 12
        period = 'PM'

    elif hour >= 1 and not period:
        hour -= 12
        period = 'PM'

    new_time = f'{hour}:{minute} {period}'

    if day:
        index = (days[day.lower()] + n_days) % 7
        day = list(days.keys())[list(days.values()).index(index)]
        new_time += f', {day.capitalize()}'

    if n_days == 1:
        return f'{new_time} (next day)'

    elif n_days > 1:
        return f'{new_time} ({n_days} days later)'

    return new_time
