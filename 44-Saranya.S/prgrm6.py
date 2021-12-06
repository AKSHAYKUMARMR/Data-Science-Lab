from datetime import date
def numOfDays(date1,date2):
    return(date2-date1).days
date1=date(2016,12,11)
date2=date(2019,2,26)
print(numOfDays(date1,date2),"days")
