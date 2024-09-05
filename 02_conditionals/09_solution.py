
# 9.Leap Year Checker:
# Prooblem : Determine  if a year is a leap year.
# (Leap year are divisible by 4, but not divisible by 100 unless also divisible by 400).

year = 2024

if (year % 400 == 0) or (year % 4 == 0  and year % 100 != 0):
    print(year,"is a Leap Year")
else:
    print(year,"Not a Leap Year")
