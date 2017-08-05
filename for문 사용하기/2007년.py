import calendar
l=['MON','TUE','WED','THU','FRI','SAT','SUN']
d=calendar.weekday(2007, *map(int, input().split()))
print(l[d])