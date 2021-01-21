import re

open_file = 'http_logs_for_analysis.txt'

with open('http_logs_for_analysis.txt', 'r') as file:
    x = file.read()
    y = '192.168.4.164' in x
    print (type(x))
    print (y)

#z= re.search(r'192.168.4.164',x)

#search only returns the first match found
z =re.search(r'\w+\.\w+',x)
print (z)

#findall returns all matches
#print (x)
#q = re.findall(r'\w+\.\w+\.\w+\.\w+', x)

#print (q)
q = re.finditer(r'\w+\.\w+\.\w+\.\w+', x)
print (next(q))
print (next(q))
print (next(q))
print (next(q))
print (next(q))
print (next(q))
print (next(q))
print (next(q))
print (next(q))