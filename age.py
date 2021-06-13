from datetime import date, timedelta

dob = date(2001, 2, 1)
age = (date.today() - dob)// timedelta(days=365.245)
print(age)
