"""
How many day's temperature? 2
Day 1's high temp: 10
Day 2's high temp: 20

Average = 15.0
1 day(s) above average
"""




def temperature():
    dayCount = int(input("How many day's temperature? "))
    temperatures = list()
    for i in range(dayCount):
        temperatures.append(int(input(f"Day {i + 1}'s high temp: ")))

    print("\n")
    average = sum(temperatures) / dayCount 
    dayAboveCount = 0
    for temp in temperatures:
        if temp >= average:
            dayAboveCount += 1
        
    print(f"Average = {average}")
    print(f"{dayAboveCount} day(s) above average")

temperature()