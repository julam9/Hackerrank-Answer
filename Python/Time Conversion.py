##Time Conversion
# Objective : Given 12 hour format, change to 24 hour format
def timeConversion(s):
    #check if in am
    if s[-2:] == 'AM':
      #special case where the time is 12:00
      if s[0:2] == '12':
        tc_result = str(s.replace('12', '00', 1))
      else : tc_result = s
    #check if in pm
    if s[-2:] == 'PM' :
      #special case where the time is 24:00
      if s[0:2] != '12':     
        tc_result = str(int(s[0:2])+12)+s[2:]
      else : tc_result = s
    return tc_result[:8]
#testing
timeConversion('01:00:09PM')
