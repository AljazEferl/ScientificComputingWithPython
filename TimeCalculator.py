def add_time(start, duration, day = ""):
    time, timeOfDay = start.split()
    startHour, startMinutes = map(int, time.split(":"))
    durationHour, durationMinutes = map(int, duration.split(":"))
    
    if timeOfDay == 'PM' and startHour != 12:
        startHour += 12
              
    totalStartMinutes = 60 * startHour + startMinutes
    #print(totalStartMinutes)

    totalDurationMinutes = 60*durationHour + durationMinutes

    #print(totalDurationMinutes)

    totalTime = totalStartMinutes + totalDurationMinutes
    #print(totalTime)

    result = totalTime / 60  
    hoursT = (totalTime // 60) % 24   
    minutesT = totalTime % 60
    
    timeOfDay = "AM" if hoursT < 12 else "PM"
    if hoursT > 12:
        hoursT -= 12
    elif hoursT  % 12 == 0:
        hoursT = 12 
        
    totalDays = int(totalTime  / (24 * 60))
    #print(int(totalDays))

    if totalDays == 0:
        dayString = ""
    elif totalDays == 1:
        dayString = " (next day)"
    else:
        dayString = f" ({totalDays} days later)"

    if day: 
        daysOfWeek = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday']
        endDay = daysOfWeek[(daysOfWeek.index(day.capitalize()) + totalDays) % 7]
        
        #print(endDay)
        return (f'{hoursT}:{minutesT:02d} {timeOfDay}, {endDay}{dayString}')
    else:    
        return (f'{hoursT}:{minutesT:02d} {timeOfDay}{dayString}')



add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)




     