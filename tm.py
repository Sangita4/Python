import time
timestamp = time.strftime('%H:%M:%S')
current_time = time.strptime (timestamp, "%H:%M:%S")

if time.strptime('04:00:00', '%H:%M:%S') <= current_time < time.strptime('12:00:00', '%H:%M:%S'):
    print("Good Morning")
elif time.strptime('12:00:00', '%H:%M:%S') <= current_time < time.strptime('16:00:00', '%H:%M:%S'):
    print("Good Afternoon")
elif time.strptime('16:00:00', '%H:%M:%S') <= current_time < time.strptime    ('20:00:00', '%H:%M:%S'):
    print("Good Evening")
else:
    print("Good Night")
