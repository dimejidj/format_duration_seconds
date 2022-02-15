def format_duration(seconds):
    #your code here
    import math
    import datetime
    sec = seconds
    second_time = str(datetime.timedelta(seconds=sec))
    
    def check_hours(min, hrs, sec):
        if hrs == 0:
            return ''
        elif hrs == 1:
            if min > 0 and sec == 0:
                return '1 hour and'
            elif min > 0 and sec > 0:
                return '1 hour,'
            else:
                return '1 hour'
        else:
            if min > 0 and sec == 0 or min == 0 and sec > 0:
                return f'{hrs} hours and'
            if min > 0 and sec > 0:
                return f'{hrs} hours,'
            else:
                return  f'{hrs} hours'

    def check_mins(min, hrs, sec):
        if min == 0:
            return ''
        elif min == 1:
            if sec > 0:
                return '1 minute and'
            else:
                return '1 minute'
        else:
            if sec > 0:
                return f'{min} minutes and'
            else:
                return f'{min} minutes'

    def check_sec(min, hrs, sec):
        if sec == 0:
            return ''
        elif sec == 1:
            return '1 second'
        else:
            return f'{sec} seconds'
        
    def show_str(hrs, min, sec):
        arr = [hrs, min, sec]
        showStr = ''
        for i in arr:
            if i == '':
                continue
            else:
                showStr += f'{i} '
        return showStr
    
    def change_num(val):
        if val == '00':
            return 0
        else:
            return int(float(val))
        
        
    if sec == 0:
        return 'now'
    elif 'days' not in second_time and 'day' not in second_time:  
        hours_unit, minute_unit, seconds_unit = second_time.split(':')
        hours_unit = change_num(hours_unit)
        minute_unit = change_num(minute_unit)
        seconds_unit = change_num(seconds_unit)

        finalStr = show_str(check_hours(minute_unit, hours_unit, seconds_unit), check_mins(minute_unit, hours_unit, seconds_unit), check_sec(minute_unit, hours_unit, seconds_unit))
        return f'{finalStr.strip()}'
    else:
        days, time_split = second_time.split(', ')
        days_fig, days_str = days.split(' ')
        hours_unit, minute_unit, seconds_unit  = time_split.split(':')
        hours_unit = change_num(hours_unit)
        minute_unit = change_num(minute_unit)
        seconds_unit = change_num(seconds_unit)
        days_fig = int(days_fig)
        years = days_fig/365
        days_left = days_fig % 365
        days_left = int(days_left)
        if days_fig < 366:
            finalStr = show_str(check_hours(minute_unit, hours_unit, seconds_unit), check_mins(minute_unit, hours_unit, seconds_unit), check_sec(minute_unit, hours_unit, seconds_unit))
            stripping = finalStr.strip()
            return f'{days}, {stripping}'
        else:
            finalStr = show_str(check_hours(minute_unit, hours_unit, seconds_unit), check_mins(minute_unit, hours_unit, seconds_unit), check_sec(minute_unit, hours_unit, seconds_unit))
            stripping = finalStr.strip()
            if int(years) == 1:
                return f'{int(years)} year, {days_left} days, {stripping}'
            else:
                return f'{int(years)} years, {days_left} days, {stripping}'
