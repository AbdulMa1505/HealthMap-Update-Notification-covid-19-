import requests
from win10toast import ToastNotifier
import json 
import time

def CovidUpdate():
    r = requests.get('https://disease.sh/v3/covid-19/all')
    data=r.json()
    text =f'confirmed cases:{data["cases"]}\nDeaths:{data["deaths"]}\nRecovered:{data["recovered"]}'
    while True:
        toast=ToastNotifier()
        toast.show_toast("covid-19 updates",text,duration=20)
        time.sleep(3600)
if __name__ == CovidUpdate()