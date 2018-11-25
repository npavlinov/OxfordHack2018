from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import sys
import requests
import json
import six
import scrap
from Paragraph import Paragraph


def getString(s1, s2):
    params={
        "text1": s1,
        "text2": s2
    }
    headers={
        "X-Mashape-Key": "swb9S2ZELsmsh8SWVp7nMrUs2NxKp1ziuTxjsnEyYj69sVinYt",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
      }
    return requests.post('https://twinword-text-similarity-v1.p.mashape.com/similarity/',
    params=params, headers=headers)

def similarity(a, b):
    return json.loads(getString(a, b).text)["similarity"]


def keywords(text):
    client = language.LanguageServiceClient()
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    entities = client.analyze_entities(document).entities
    out=[]
    for e in entities[:3]:
        out.append(e.name)
        
    return out





# MAIN COMPILE FUNCTION
def compile(input_names, output_name, folder='Biology'):
    print(input_names)
    para=[]
    for nb, file_name in enumerate(input_names):
        file=open(file_name, 'r')
        txt=file.read()
        
        #delete the titles
        b=txt.find('##')
        while b!=-1:
            e=txt.find('\n', b)
            txt=txt[:b]+txt[e:]
            b=txt.find('##')
            
        #replace the links by the websites scrapped
        b=txt.find('$')
        while b!=-1:
            e1=txt.find('\n', b)
            e2=txt.find(' ', b)
            link=txt[b+1:e2]
            arg=txt[e2+1:e1]
            #print(link, ';', arg)
            website = scrap.get_from_url(link, int(arg))
            #print(website)
            txt=txt[:b]+website+txt[e1:]
            b=txt.find('$')
        
        #extract paragraphes
        txt=txt.split('\n\n')
        for i, p in enumerate(txt):
            p=p.replace('\n', '').replace('\t', '')
            para.append(Paragraph(file_name, i, keywords(p), p))
        file.close()


    newPara = []
    while len(para) > 0:
        sameKeyWrdPara = [Paragraph(para[0].file, para[0].nb, para[0].keywords, para[0].text)]
        i=1
        while i<len(para):
            p=para[i]
            if para[0].eq(p):
                sameKeyWrdPara.append(Paragraph(p.file, p.nb, p.keywords, p.text))
                para.remove(p)
            else:
                i+=1
        para.remove(para[0])
        newPara.append(sameKeyWrdPara)

    # for p in newPara:
    #     print(p)

    for paras in newPara:
        j=0
        while j<len(paras):
            i=j+1
            while i<len(paras):
                simEval=similarity(paras[j].text,paras[i].text)
                if simEval>=0.75:
                    paras.remove(paras[i])
                else:
                    i+=1
            j+=1
            
    
    #print(" ")
    #for p in newPara:
    #    print(p)

    output=open(output_name, 'w')
    output.write('# '+folder+'\n')
    for paras in newPara:
        if len(paras)>1:
            output.write('\n## ' + " ".join(paras[0].common(paras[1]))+'\n')
        elif len(paras[0].keywords)>0:
            output.write('\n## ' + paras[0].keywords[0]+'\n')
        for p in paras:
            if len(p.text)>5:
                output.write("\t"+p.text+"\n")
    output.close()

    #print(" ")
    #print(open("out.txt", 'r').read())


import os
if __name__=='__main__':
    folder=sys.argv[1]
    dir = os.getcwd()
    compile([dir+"/writeTo/"+folder+"/notes.md", dir+"/back/new_notes.txt"], \
            dir+"/writeTo/"+folder+"/notes.md", folder)
    


