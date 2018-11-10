import re
food = "hat rat mat pat"
regex = re.compile("[r,m]at")

food = regex.sub("food",food)

print(food)
