import requests
import webbrowser

dest = 'index.html'


r = requests.get('https://app.mobalytics.gg/fr_fr/lol/profile/euw/balthazar%20cla%C3%ABs/overview')
destination_file = open(dest, "a", encoding="utf-8")
destination_file.truncate(0)
destination_file.write(r.text)
destination_file.close()
file = webbrowser.open(dest) 