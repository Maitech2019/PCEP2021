#rainfall

years = []
rainfalltotal = 0
count = 0

for year in range(1,3):
    print("Year", year)
    for month in range(12):
        count = count + 1
        rainfall = float(input("Enter the raianfall amount for the month: "))
        rainfalltotal = rainfalltotal + rainfall


average = rainfall/count
        
print("For", count, "month")
print("Total rainfall: ",rainfalltotal, "inch")
print("Average monthly rainfall: {:.2f}".format(average), "inches")

    
