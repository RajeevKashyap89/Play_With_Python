import json
open()

f = open('work-file','r',encoding="utf-8")

print(f.read())



####################################

# Printing in the format of Json
x = [1, 'simple', 'list']
print(json.dumps(x))