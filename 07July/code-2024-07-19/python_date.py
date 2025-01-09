

import datetime as dt

now = dt.datetime.now()

today = dt.datetime.today()

# print(now)
# print(today)



# making own date

birth_date = dt.date(1992, 2, 24)
birth_datetime = dt.datetime(1992, 2, 24, 10, 30, 44)

event_datetime = dt.datetime(year=2004, day=2, month=8, hour=10, minute=30, second=44)
event_date = dt.date(year=2024, month=2, day=24)

# print(birth_date)
# print(birth_datetime)

# print(event_date)
# print(event_datetime)

# print(type(event_date))
# print(type(event_datetime))


# print(event_date.year)                      # only year gonna come in output
# print(event_date.month)   




# creating date for future


     #timedelta
difference_days = dt.timedelta(400)     


# future_date = event_date + difference_days
# print(event_date)
# print(future_date)


future_datetime = event_datetime + difference_days

# print(event_date)
# print(future_datetime)




#creating date for past

# print(today)
# past_datetime = today - difference_days

# print(past_datetime)




valentines_day = dt.datetime(year=2024, month=2, day=14)


# print(valentines_day)


valentines_datetime = dt.datetime(year=2024, month=2, day=14, hour=20, minute=30)


# print(valentines_datetime)


text = 'This year valentines day was on 14th of February, 2024.'


text_datetime = dt.datetime.strptime(text, 'This year valentines day was on %dth of %B, %Y.')

# print(text_datetime)

vacation = '2024/07/28 14:20:33'

vacation_datetime = dt.datetime.strptime(vacation, '%Y/%m/%d %H:%M:%S')


print(vacation_datetime)


# travel_text = dt.datetime.strftime(vacation_datetime, 'We will travel on %Y/%m/%d %H:%M:%S')

travel_text = dt.datetime.strftime(vacation_datetime, 'We will travel on %dth %b, %Y at %I:%M:%S %p')

travel_txt = vacation_datetime.strftime('We will travel on %dth %b, %Y at %I:%M:%S %p')       #another way to write

# print(travel_text)


















