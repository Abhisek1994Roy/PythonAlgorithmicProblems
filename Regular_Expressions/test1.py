import re


str = "we need to inform him the latest information"
if re.search("inform", str):
    print("There is inform")


allinform = re.findall("inform", str)
for i in allinform:
    print (i)
    
for i in re.finditer("inform",str):
    loctup = i.span()
    print(loctup)
