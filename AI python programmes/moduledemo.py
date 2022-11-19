import imp
 
import module
import datetime as dt
 
module.welcome('harsh')
 
print('Employee Details: ', module.employee["name"], "  ", module.employee["age"], "  ", module.employee["profile"])
 
datetime = dt.datetime.now()
 
print(datetime.year)
print(datetime.month)
print(datetime.day)