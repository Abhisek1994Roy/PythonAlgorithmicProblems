import urllib.request, urllib.parse, urllib.error

file_handler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')


counts={}
for line in file_handler:
    words=(line.decode().strip())
    words=words.split(" ")
    for word in words:
        counts[word] = counts.get(word,0)+1
print(counts)
