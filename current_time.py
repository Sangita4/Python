# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

import datetime 
c_time = datetime.datetime.now() #%Y-%M-%D %H:%m:%S)
print(c_time.strftime("%Y-%m-%d %H:%M:%S"))
print(c_time.strftime("%D"))
