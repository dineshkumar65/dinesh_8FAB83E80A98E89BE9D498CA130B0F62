print("Program to check whether the given year is leap year or not")
year = int(input("Enter the year:"))
if (year % 4 == 0):
  print("The Given year", year, "is a leap year")
else:
  print("The Given year", year, "is not a leap year")