import re

randstr="12345"
print("Matches :",len(re.findall("\d",randstr)))
print("Matches :",len(re.findall("\D",randstr)))

#\d will match any number
#\D will match anything but a number
