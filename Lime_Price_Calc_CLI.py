# Lime Price Calc
# 55 huf/min
from geopy.distance import geodesic
minute_cost = 55
speed = 250

start = (input('\nWhere from? (coordinates)\n'))
dest = (input ('\nWhere to?\n'))


road = ((geodesic(start, dest).kilometers))
if road < 1:
    road2 = ((geodesic(start, dest).meters))
    print (road2, "m \n")
    time = (road2 / speed)
    print ('\n' , time , " minutes")
    cost = (time*minute_cost)
    print ('\n', cost, "HUF")
if road > 1:
    print (road, "m \n")
    time = (road * speed)
    print ('\n' , time , " minutes")
    cost = (time*minute_cost)
    print ('\n', cost, "HUF")

