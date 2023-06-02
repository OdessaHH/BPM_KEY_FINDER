
import datetime
now = datetime.date.today()
print("enter a start counting date. ")

d = int(input("please enter a day: "))
m = int(input("please enter a month: "))
y = int(input("please enter a year: "))
then = datetime.date(y, m, d)

print("your date was: ",then)
print("today is: ",now)
#print(type(then))
#print(type(now))

delta_days = now - then
#print("Since your date passed ",delta_days)
#print(type(delta_days))


from dateutil.relativedelta import relativedelta
rdelta = relativedelta(now, then)
print('years passed since: ', rdelta.years)
print('months passed since: ', rdelta.months)
print('days passed since: ', rdelta.days)

#print(type(relativedelta))

print("Since your date passed ",rdelta.years, " years, ",rdelta.months, " months and ", rdelta.days, "days or ", delta_days, " days")


