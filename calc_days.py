import _pytest
def date_diff():
    import datetime
    from datetime import date
    now = datetime.datetime.now().date()
    # print(now)
    in_date = input("Enter date in the format (YYYY-MM-DD) :")
    yr, mon, days = map(int, in_date.split('-'))
    date1 = datetime.date(yr, mon, days)
    diff_day = (now - date1).days
    print("No.of days between the given and present day are:", diff_day)


date_diff()
