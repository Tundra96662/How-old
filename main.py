def MonthsInYears(years):
    totalMonths = years * 12
    return totalMonths

def DaysInMonths(months):
    totalDays = months * 30
    return totalDays
    
def HoursInDays(days):
    totalHours = days * 24
    return totalHours
    
def MinutesInHours(hours):
    totalMinutes = hours * 60
    return totalMinutes
    
def SecondsInMinutes(minutes):
    totalSeconds = minutes * 60
    return totalSeconds
    
def TotalTime(num):
    print("You are " + str(num) + " years old")
    
    months = MonthsInYears(num)
    print("That means you are " + str(months) + " months old,")
    
    days = DaysInMonths(months)
    print("or " + str(days) + " days old,")
    
    hours = HoursInDays(days)
    print("or " + str(hours) + " hours old,")
    
    minutes = MinutesInHours(hours)
    print("or " + str(minutes) + " minutes old,")
    
    seconds = SecondsInMinutes(minutes)
    print("or " + str(seconds) + " seconds old.")
    
    
TotalTime(16)
