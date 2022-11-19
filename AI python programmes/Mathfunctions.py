from cmath import sqrt
import math
import time

x = pow(2,3)

print(x)

y = sqrt(625)

print(type(y))

pi = math.pi

print(pi)

print(math.floor(2.9)) # gives 2 (lowest value)
print(math.floor(2.2)) # gives 2 (highest value)
print(math.ceil(2.2)) # gives 3  (highest value)

print(time.time())

print(time.localtime())

current_time = time.localtime(time.time())

print("Local current time :", current_time)

