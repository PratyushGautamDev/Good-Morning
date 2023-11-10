import time 

current_time = time.strftime('%H:%M:%S')
print(current_time)

hour = int(time.strftime('%H'))
print("The current hour time is", hour)

if hour > 0 and hour <= 12:
    print('Good Morning')
elif hour > 12 and hour <= 18:
    print('Good Afternoon') 
else:
    print('Good Night')