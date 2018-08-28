import json
import os
import sys
# print(extension_arr)





def show_config(extension_arr):
    for row in extension_arr:
        for key, value in row.items():
            print(key,"--->",value)
        print("-------------------------------------------")

def get_root():
    root_folder = input("Enter root folder or drive:-  ")
    for root, dirs, files in os.walk(root_folder):
        path = root.split(os.sep)
        # print((len(path) - 1) * '--', os.path.basename(root))
        print((len(path) - 1) * '--', os.path.abspath(root))
        for file in files:
            print(len(path) * '--', os.path.abspath(file))

with open('config.json') as extension_types:
    extension_arr = json.load(extension_types)
choice=999
while choice!=1 and choice!=2:
    choice = int(input("Enter 1 to show config, or 2 to get root."))
    if choice!=1 and choice!=2:
        print("Wrong option selected. Try again")

if choice == 1:
    show_config(extension_arr)
elif choice == 2:
    get_root()
# elif choice == 3:
#     os.mkdir(path)
