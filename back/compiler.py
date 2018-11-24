import sys
import requests
import json
#from similar import *
import API
from Paragraph import Paragraph

def similarity(a, b):
    return json.loads(API.getString(a, b).text)["similarity"]

def keywords(txt):
    return []

if len(sys.argv)==1:
    files_names = ['first.txt', 'second.txt']
else:
    files_names = sys.argv[1:]
print(files_names)



para=[]
for nb, file_name in enumerate(files_names):
    print(file_name)
    file=open(file_name, 'r')
    txt=file.read()
    txt=txt.split('\n\n')
    para.append([])
    for i, p in enumerate(txt):
        para[nb].append(Paragraph(file_name, i, keywords(p)))
    file.close()

print(para)



output=open("out.txt", 'w')
output.write("\tThis is our result:\n\n")

output.close()
    

print(open("out.txt", 'r').read())






