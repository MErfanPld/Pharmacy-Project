from . import jalali
from django.utils import timezone
from datetime import datetime, date

def persion_numbers_converter(mystr):
    numbers = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }
    for e, p in numbers.items():
        mystr = mystr.replace(e, p)
    return mystr

def jalali_converter(time):
    jmonths = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']

    if isinstance(time, datetime):
        time = timezone.localtime(time)
    elif isinstance(time, date):
        time = datetime.combine(time, datetime.min.time())
        time = timezone.make_aware(time, timezone.get_current_timezone())
    else:
        raise ValueError("Expected a date or datetime object")

    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()

    time_to_list = list(time_to_tuple)

    for index, month in enumerate(jmonths):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    output = "{} {} {}".format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0]
    )
    return persion_numbers_converter(output)
