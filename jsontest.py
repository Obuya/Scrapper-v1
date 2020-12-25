import json
import re


with open("pre.json", "r") as f:
    data=f.read()
    
obj = json.loads(data)

keys = list(obj.keys())
for i in range(len(obj)):
    test = obj.get(keys[i])
    text = obj.get(keys[i])['Prerequisites'] 
    if text.find("Course credit exclus") != -1:
        text = text[0: text.index("Course credit exclus")]
    pres = re.findall('([A-Z]*/[A-z]*(\s|)[0-9]*\s.\...)', text)
    for i in range(len(pres)):
        pres[i] = pres[i][0]
    test.update({"Prerequisites" : pres})
    print('After: ' + str(pres) + "\n")

with open('testing.json', 'w') as fp:
    json.dump(obj, fp)  