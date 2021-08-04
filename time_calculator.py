def add(start_time, new_time, day=None):

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

    old_hour = start_time.split(':')[0]
    old_minute = start_time.split(':')[1].split()[0]
    old_period = start_time.split()[-1]

    new_hour = new_time.split(':')[0]
    new_minute = new_time.split(':')[1]
    n_days = int((old_hour + new_hour) / 24)

    hour = old_hour + new_hour
    minute = old_minute + new_minute

    if minute >= 60:
        hour += 1
        minute %= 60

    

add('1:00 AM', '2')