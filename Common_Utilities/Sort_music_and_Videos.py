import json
import os
import sys

def show_config(extension_arr):
    for row in extension_arr:
        for key, value in row.items():
            print(key,"--->",value)
        print("-------------------------------------------")

def get_root(extension_arr):
    root_folder = input("Enter root folder or drive:-  ")
    # print(os.path.abspath(root_folder))
    root_path = os.path.abspath(root_folder)
    for media_types in  extension_arr:
        new_folder = root_path+os.sep+media_types["Media"]
        print(new_folder)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

    for root, dirs, files in os.walk(root_folder):
        # print(os.sep)
        # path = root.split(os.sep)
        # print(path)
        # Uncomment line below this to print the folders
        # print((len(path) - 1) * '--', os.path.abspath(root))
        for file in files:
            # Uncomment line below to print files
            # print(len(path) * '--', os.path.abspath(file))
            # print(os.path.abspath(file))
            pass



def main():
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
        get_root(extension_arr)

if __name__ == "__main__":
    main()
