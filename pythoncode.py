#by Krimy Tarpara coded on 4 June 2023
#It ask the user for a date between 1970 and 2100 and determines and displays
#the day on that date
#whether it is leap year or non-leap year


Date= input("Enter date in the form dd/mm/yyyy : \n").split('/') #user will enter the date 
DaysOfMonth = int(Date[0]) # it can vary from 1 to 31
Month = int(Date[1]) # it can vary from 1 to 12
Year = int(Date[2]) # it is from 1970 to 2100 
# using Boolean
isLeapYear="non-leap"
validyear = False
validMonth = False
validDay = False

extraDays = 0
extraDaysDueToYears = 3 

if Month == 1:
    extraDays = 0

elif Month == 2:
    extraDays = 31

elif Month == 3:
    extraDays = 59 #assuming it is a non-leap year

elif Month == 4:
    extraDays = 90

elif Month == 5:
    extraDays = 120

elif Month == 6:
    extraDays = 151

elif Month == 7:
    extraDays = 181

elif Month == 8:
    extraDays = 212

elif Month == 9:
    extraDays = 243

elif Month == 10:
    extraDays = 273

elif Month == 11:
    extraDays = 304

elif Month == 12:
    extraDays = 334
    

extraDays = extraDaysDueToYears + extraDays - 1 
totalDifferenceOfDays = extraDays + DaysOfMonth
offset = totalDifferenceOfDays % 7
DayOfTheWeek ="Thursday"

if offset == 0:
    DayOfTHeWeek = "Thursday"
if offset == 1:
    DayOfTheWeek="Friday"
elif offset == 2:
    DayOfTheWeek="Saturday"
elif offset == 3:
    DayOfTheWeek="Sunday"
elif offset == 4:
    DayOfTheWeek="Monday"
elif offset == 5:
    DayOfTheWeek="Tuesday"
else :
    DayOfTheWeek="Wednesday" # end conversation from offset to name of the day


#check valid year
if Year<1970 or Year>2100:
    validyear=False
else:
    validyear=True

#check leap year
if Year % 4 ==0 and not Year % 100 ==0 or Year % 400 ==0:
    isLeapYear="leap"
else:
    isLeapYear="non-leap"

#check valid month
if Month>12 or Month < 1:
    validMonth = False
else:
    validMonth=True

#check valid day
if Month in (1,3,5,7,8,10,12) and DaysOfMonth>31: #month which contain 31 days.
    validDay = False
elif Month in (4,6,9,11) and DaysOfMonth>30: #month which contain 30 days.
    validDay = False
elif Month ==2 and DaysOfMonth>29: #february which contain 29 days as it is leap year.
    validDay = False
elif Month==2 and isLeapYear=="non-leap" and DaysOfMonth>28: #february which contain 28 days as it is non-leap year. 
    validDay = False
else:
    validDay=True


#if the year is outside the valid range.
if not validyear:
    print("Sorry!," + str(Year) + " is outside the valid range")
#if the month is outside the valid range.
if not validMonth:
    print("Sorry!," + str(Month) + " is outside the valid range")
#if the day of month is outside the valid range.
if not validDay:
    print("Sorry!," + str(DaysOfMonth) + " is outside the valid range")

#if the year, month and the day of the month is correct.
if(validDay and validMonth and validyear):
    print("Date" + "       : " + "Day")
    print("-"*23)
    print("/".join(Date) + " : " + DayOfTheWeek) #for a date.
    print(str(Year) + " is a " + isLeapYear + " year") #for a leap or non-leap year.
    print("Thank You!")
