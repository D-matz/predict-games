import json
import os

f = open('renamerunes.txt')

def search_and_rename(sub_json):
    for j in sub_json:
        if not isinstance(j, str) and not isinstance(j, int):
            if 'icon' in j:
                filename = os.path.basename(j['icon'])
                print(j['id'], filename)
                if os.path.exists(filename):
                    os.rename(filename, str(j['id']) + ".png")
            search_and_rename(j)
        else:
            newjson = sub_json[j]
            if not isinstance(newjson, str) and not isinstance(newjson, int):
                search_and_rename(newjson)

data = json.load(f)
search_and_rename(data)
