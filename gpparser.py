import urllib.request, json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

list = []
with urllib.request.urlopen("https://www.gamerpower.com/api/giveaways?platform=pc") as url:
    data = json.loads(url.read().decode())
    for i in data:
        list.append(i['worth'] + " " + i['title']  + " " + i['open_giveaway'] + " " + i['platforms'] + " " + i['type'])

list = sorted(list, reverse=True)

for i in list:
    print(i)