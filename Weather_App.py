import requests
import json
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
city = input("Enter the name of the city = ")
url = f"https://api.weatherapi.com/v1/current.json?key=52a9385c8f2b4fe6864170644240504&q={city}"
r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

s=f"The current weather of {city} is {w} degree"
print(s)
speaker.Speak(s)