from datetime import date
def numOfDays(f_date,l_date):
    return(l_date-f_date).days
f_date=date(2014,7,2)
l_date=date(2014,7,11)
print(numOfDays(f_date,l_date),"days")
