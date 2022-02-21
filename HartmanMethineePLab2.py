# Magic date programm

month = int(input("Enter the month in numeric form: "))
date = int(input("Enter the day of the month: "))
year = int(input("Enter the year in two digit format: "))

print("The date is {} / {} / {}".format(month,date,year))

if month*date == year:
    answer = "This is a magic date."
else:
    answer = "This is not a magic date."

print(answer)
print("press enter")



