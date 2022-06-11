import json
import os

f = open('renamespell.txt')

def search_and_rename(sub_json):
    for k in sub_json:
        print("try",sub_json[k])
        j = sub_json[k]
        if not isinstance(j, str) and not isinstance(j, int):
            if 'id' in j:
                filename = j['id']
                num = j['key']
                print(j['id'], filename)
                if os.path.exists(filename):
                    os.rename(filename, num + ".png")
            search_and_rename(j)
        else:
            try:
                newjson = sub_json[k]
                if not isinstance(newjson, str) and not isinstance(newjson, int):
                    search_and_rename(newjson)
            except:
                for z in newjson:
                    pass
                    #print(k)

data = json.load(f)
for ss in data['data']:
    sj = data['data'][ss]
    filename = sj['id']+".png"
    num = sj['key']
    print(num, filename)
    if os.path.exists(filename):
        os.rename(filename, num + ".png")
