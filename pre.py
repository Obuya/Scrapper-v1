# Python program to read 
# json file 
  
  
import json 
  
# Opening JSON file  

with open('courses1.json', 'r') as f:
    distros_dict = json.load(f)

for distro in distros_dict.items():
    print(distro[0])
f.close() 