##Grading Students
# Objective : Round the original grade to final grade
# Conditions :
#- Under 40 wont be rounded
#- If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
#- If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade
def gradingStudents(grades):
    return [g+(g > 37)*(g % 5 > 2)*(5 - (g % 5)) for g in grades] 
#testing
gradingStudents([38,39,40,41,42])