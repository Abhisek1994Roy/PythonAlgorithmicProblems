import re
randstr = '''
Keep the blue flag
flying high
Chelsea
'''
print(randstr)
regex = re.compile("\n")
randstr = regex.sub(" ",randstr)
print(randstr)

#\b: backspace
#\f: formfeed
#\r: carriage return
#\t: Tab
#\v: Vertical Tab
