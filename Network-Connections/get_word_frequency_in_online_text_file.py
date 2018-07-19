#This program will help you access a text file which is in web and count the
#frequency of each word in it
import urllib.request, urllib.parse, urllib.error

file_handler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')


counts={}
for line in file_handler:
    words=(line.decode().strip())
    words=words.split(" ")
    for word in words:
        counts[word] = counts.get(word,0)+1
print(counts)
