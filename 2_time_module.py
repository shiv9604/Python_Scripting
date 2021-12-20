
import time

''' 
epic time = time in seconds from 1jan 1970 till today
'''
# epic time in seconds which doesnt makes sence to us
epic = time.time() # --> this will give the time in secods from epic time
print(epic)

#Time in the format the makes sense to us
localtime =  time.localtime() # --> (tm_year=2021, tm_mon=6, tm_mday=8, tm_hour=1, tm_min=58, tm_sec=37, tm_wday=1, tm_yday=159, tm_isdst=0)
print(localtime)

#Exact what we want in the local time format???
print(localtime.tm_year) # --> tm_ gives us flexibility to us for the things what we want from the format....

# This things in best formatted way
print(time.ctime(epic)) # --> day:month:date:Time:year


