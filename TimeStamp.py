import time
import datetime

current_time = time.time()
print(current_time)
st = datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')
print(st)


#Calculating 60 days 40 seconds 10 minutes 10 hours before
#start_date = datetime.datetime.now() + datetime.timedelta(-60,40,0,0,-10,-10)
start_date = datetime.datetime.now() + datetime.timedelta(-60,40)
#start_date = datetime.datetime.fromtimestamp(start_date).strftime('%Y-%m-%d %H:%M:%S')
print("60 days 10 before is ",start_date)


#Comparing date stamps
past = start_date
present = datetime.datetime.now()
print(present > past)
