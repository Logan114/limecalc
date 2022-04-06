import PySimpleGUI as sg
minute_cost = 55
from geopy.distance import geodesic
minute_cost = 55
speed = 15
km=10**3
min = 60

sg.theme('DarkAmber')
layout = [ [ sg.Text("Where from?"), sg.InputText()],
    [sg.Text("Where to?"), sg.InputText()],
    [sg.Text("Speed? (Default: 15km/h)"), sg.InputText(15,3)],
    [sg.Text ("cost: ")], [sg.Output(key="cost", size=(15,1))],
    [sg.Text ("time: ") ], [sg.Output(key="time", size=(15,1))],
    [sg.Text ("Distance:")], [sg.Output(key="distance", size=(15,1))], 
    [sg.Button('Calc')], [sg.Button('Exit')]]

cost = layout

window = sg.Window("Lime ride price calculator", layout)
event, value = window.read()

while True:
    
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    start = (values[0]) # starting coordinates
    dest = (values[1]) # Destination coordinates
    speed = int(values[2]) #Speed, could be left empty
    
    road = ((geodesic(start, dest).kilometers))
    
    road2 = ((geodesic(start, dest).meters))
    mpm = ((speed*km)/min) # Meter Per Minute
    time = (road2 / mpm) # Time it takes for the road to be taken
    cost = (time*minute_cost)
    road_final = float(road)
    road_final = "{:.2f}".format(road_final) # 2 Decimal places for the road thingy
    if road < 1:
        road_final = float(road2)
        road_final = "{:.2f}".format((road_final))
        window['distance'].update(road_final +  "m")
    if road > 1:
        window['distance'].update(road_final + "km")

    
    time = float(time)
    time = "{:.2f}".format(time)
    cost = float(cost)
    cost = "{:.0f}".format(cost)
    window['cost'].update(cost + " Ft")
    window['time'].update(time + " Min")
 
window.close()
