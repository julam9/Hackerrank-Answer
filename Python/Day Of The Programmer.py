## Day of the Programmer  
# Objective : Tell the date of the 256th day of the year using Russian Callendar.
# Constraints : 1700 <=Years <=2700 

def dayOfProgrammer(year):
    #for Julian Calendar (1700-1917) 
    if year in range(1700, 1918):
        #check if its leap year 
        if year%4 == 0:
            return(f"12.09.{year}")
        #if not leap year
        else : 
            return(f"13.09.{year}")
    #for Transition Year (1918)
    elif year == 1918:
        return("26.09.1918")
    #for Gregorian Calendar
    else : 
        #check if it leap year    
        if year%400 == 0 or (year%4==0 and year%100!=0):
            return(f"12.09.{year}")
        #if not leap year
        else:
            return(f"13.09.{year}") 
#testing 
dayOfProgrammer(2017)
dayOfProgrammer(1800) 
dayOfProgrammer(1917)