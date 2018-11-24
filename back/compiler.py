import sys
import requests
import json

##print("This is the name of the script: ", sys.argv[0])
##print("Number of arguments: ", len(sys.argv))
##print("The arguments are: " , str(sys.argv))

if len(sys.argv)==1:
    files_names = ['first.txt', 'second.txt']
else:
    files_names = sys.argv[1:]
print(files_names)



output=open("out.txt", 'w')
output.write("\tThis is our result:\n\n")

para=[]
for file_name in files_names:
    file=open(file_name, 'r')
    txt=file.read()
    #output.write(txt)
    #output.write('\n')
    para.append(txt.split('\n\n'))
    file.close()

print(para)

i=0
while len(para[0])>0:
    #compare
    headers={
        "X-Mashape-Key": "swb9S2ZELsmsh8SWVp7nMrUs2NxKp1ziuTxjsnEyYj69sVinYt",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
      }
    params={
        "text1": str(para[0][i]),
        "text2": str(para[1][i])
        }
    r = requests.post('https://twinword-text-similarity-v1.p.mas\
    hape.com/similarity/', params=params, headers=headers)
    j=json.loads(r.text)
    print(j)
    if j['similarity']>0.8:
        output.write(para[0][i])
    else:
        output.write(para[0][i])
        output.write(para[1][i])
    i+=1

    

output.close()
    

print(open("out.txt", 'r').read())






