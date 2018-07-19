#This program will help you access a text file which is in web
import urllib.request, urllib.parse, urllib.error

file_handler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in file_handler:
    print(line.decode().strip())
