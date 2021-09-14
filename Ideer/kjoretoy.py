import requests

url = 'https://www.vegvesen.no/ws/no/vegvesen/kjoretoy/felles/datautlevering/enkeltoppslag/kjoretoydata'

x = requests.get(url, headers = {"SVV-Authorization": "Apikey 9c2c608c-e83c-46ab-86af-d88902e3ac15"})

print(x)

input("BLA BLa")