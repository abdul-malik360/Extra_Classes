from datetime import date, timedelta

dob = date(2000, 2, 3)
age = (date.today() - dob // timedelta(days=365.245))
print(age)
