import datetime as dt    # This is a preinstalled module in python and we don't need to install them explicitly.

# Inside this datetime module, there is a class called datetime.
# The module name and the class name is exactly same we kept an alias name for datetime module as dt in the above.

now = dt.datetime.now()        # now variable will store the current date and time. For Eg: 2023-03-12 10:58:16.627504
print(now)
print(type(now))                # type = datetime.datetime

year = now.year              # year variable will store the current year. For Eg: 2023
print(year)
print(type(year))                # type = Integer

month = now.month           # month variable will store the current month. For Eg: 03
print(month)
print(type(month))                # type = Integer

day = now.day             # date variable will store the current date. For Eg: 12
print(day)
print(type(day))                # type = Integer

hour = now.hour             # hour variable will store the current hour. For Eg: 11
print(hour)
print(type(hour))                # type = Integer

minute = now.minute         # minute variable will store the current minute. For Eg: 16
print(minute)
print(type(minute))                # type = Integer

second = now.second            # second variable will store the current second. For Eg: 6
print(second)
print(type(second))                # type = Integer

microsecond = now.microsecond   # microsecond variable will store the current microsecond. For Eg: 98425
print(microsecond)
print(type(microsecond))                # type = Integer

day_of_the_week = now.weekday()         # weekday is function and parentheses must be used.
# If sunday then day_of_the_week will hold 6 as because computer indexing starts with 0. So, If the value is 0 then it is Monday.
print(day_of_the_week)

today = dt.datetime.today()     # same as now function
print(today)

date_of_birth = dt.datetime(year=2002, month=8, day=15)     # year, month and day are the the mandatory field to be filled up. Missing any of the three field will throw an error.
print(date_of_birth)        # It will print 2002-08-15 00:00:00
# If hour, minute and second is not passed in the parameter then by default it will take it as 00 as shown above in the comment.

date_of_birth = dt.datetime(year=2022, month=8, day=15, hour=8, minute=42, second=40)
print(date_of_birth)        # It will print 2022-08-15 08:42:40

