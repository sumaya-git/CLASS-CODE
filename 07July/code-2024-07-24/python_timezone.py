
import datetime as dt

# from datetime import datetime

holiday = dt.datetime(2024, 7, 27, 10, 30, 44)
holiday_timestamp = holiday.timestamp()


# print(holiday)

# print(holiday_timestamp)




# early_date_timestamp = dt.datetime(1970, 1, 1, 0, 0, 0).timestamp()


# print(early_date_timestamp)


current_timestamp = dt.datetime.now().timestamp()

# print(current_timestamp)




time_seconds = 2314832170

# time_seconds_datetime = dt.datetime.fromtimestamp(1154355363)

time_seconds_datetime = dt.datetime.fromtimestamp(time_seconds)


# print(time_seconds_datetime)

# print(time_seconds_datetime.strftime('Date: %Y/%m/%d \nTime: %H:%M:%S %p'))




#######################
#Timezone

citric = dt.timedelta(hours=-7)

citric_tz = dt.timezone(citric)

# music_concert = dt.datetime(2024, 11, 22, 20, 30, 44, tzinfo=citric_tz)

# print(music_concert)



# import pytz


# utc_tz = pytz.utc

# estern_tz = pytz.timezone('US/Eastern')

# music_concert_utc = dt.datetime(2024, 11, 22, 20, 30, 44, tzinfo=utc_tz)

# print(music_concert_utc)


import pytz

utc_tz = pytz.utc

eastern_tz = pytz.timezone('US/Eastern')

pacific_tz = pytz.timezone('Pacific/Fiji')

music_concert_utc = dt.datetime(2024, 11, 22, 20, 30, 44, tzinfo=utc_tz)

# music_concert_est = dt.datetime(2024, 11, 22, 20, 30, 44, tzinfo=eastern_tz)

music_concert_est = music_concert_utc.astimezone(eastern_tz)

music_concert_pcf = music_concert_utc.astimezone(pacific_tz)

music_concert_pcf2 = music_concert_est.astimezone(pacific_tz)


# print(music_concert_utc)

# print(music_concert_pcf)

# print(music_concert_est)





current_time = dt.datetime.now()

kolkata_time = pytz.timezone('Asia/kolkata')

kol_time = current_time.astimezone(kolkata_time)

# print(kol_time)






import dateutil

eu_tz = dateutil.tz.gettz('Europe/Berlin')

october_festival = dt.datetime(2024, 10, 1, )














