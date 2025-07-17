#import calendar
#print(calendar.calendar(2025))

#import calendar
#print(calendar.isleap(2025))

from datetime import datetime
a=input("enter first date(YYYY-MM-DD):")
b=input("enter second date(YYYY-MM-DD):")
d1=datetime.strptime(a,"%d-%m-%y")
d2=datetime.strptime(b,"%d-%m-%y")
diff = d2 - d1
print("Difference:",abs(diff.months), "days")