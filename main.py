import requests, PySimpleGUI, ast

#Burl = lat 43.3 lon -79.8

def getWeather(Lon : float, Lat: float):
    api_url = f'https://api.api-ninjas.com/v1/weather?lat={Lon}&lon={Lat}'
    response = requests.get(api_url, headers={'X-Api-Key': 'API-KEY'})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return []
    

# define the GUI
# GUI = Graphical User Interface

layout = [ 
    [PySimpleGUI.Text("Long")],
    [PySimpleGUI.Input(key='Lon')],
    [PySimpleGUI.Text("Lat")],
    [PySimpleGUI.Input(key="Lat")],
    [PySimpleGUI.Button('Submit')],
    [PySimpleGUI.Text(size=(40, 1), key="temp")],
    [PySimpleGUI.Text(size=(40, 1), key="feel")],
    [PySimpleGUI.Text(size=(40, 1), key="max")],
    [PySimpleGUI.Text(size=(40, 1), key="min")],
    [PySimpleGUI.Text(size=(40, 1), key="humidity")],
    [PySimpleGUI.Text(size=(40, 1), key="wind")]


]

window = PySimpleGUI.Window('WeatherApp', layout)


while True:
    events, values = window.read()
    if events == PySimpleGUI.WINDOW_CLOSED or events == "Quit":
        break
    elif events == "Submit":
            try: 
                weather = getWeather(float(values['Lon']), float(values['Lat']))
                text = f"""
                
                
                Min Tempature:{weather['min_temp']}
                Humidity:{weather['humidity']}
                Wind Speed:{weather['wind_speed']}
                """
                window["temp"].update(f"Temperature:{weather['temp']}C")
                window["feel"].update(f"Feels Like:{weather['feels_like']}C")
                window["max"].update(f"Max Temperature:{weather['max_temp']}C")
                window["min"].update(f"Min Temperature:{weather['min_temp']}C")
                window["humidity"].update(f"Humidity:{weather['humidity']}%")
                window["wind"].update(f"Wind Speed:{weather['wind_speed']}km/hr")
            except ValueError:
                window["output"].update("Error")

window.close()
