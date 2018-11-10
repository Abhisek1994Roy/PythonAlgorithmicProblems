import re

Nameage='''
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21
'''

ages = re.findall(r'\d{1,3}', Nameage)
names = re.findall(r'[A-Z][a-z]*', Nameage)

ageDict={}

for x,eachname in enumerate(names):
    ageDict[eachname] = ages[x]

print(ageDict)
