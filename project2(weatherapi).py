import requests
import json
import win32com.client as wincom

speak= wincom.Dispatch("SAPI.SpVoice")
city= input("Enter the name of the city : ")

url = f"https://api.weatherapi.com/v1/current.json?key=f087e751d00941d5921165409230310&q= {city}"

r=requests.get(url)
#print(r.text)
wdic=json.loads(r.text)

w=wdic["current"]["temp_c"]
print(w)
speak.Speak((f"Current weather of {city} is {w} degrees"))



