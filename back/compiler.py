from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import sys
import requests
import json
import six
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
def compile(input_names, output_name):
    para=[]
    for nb, file_name in enumerate(files_names):
        file=open(file_name, 'r')
        txt=file.read()
        #print(file_name+":")
        #print(txt)
        txt=txt.split('\n\n')
        for i, p in enumerate(txt):
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

    for p in newPara:
        i=1
        while i<len(p):
            simEval=similarity(p[i-1].text,p[i].text)
            if simEval>=0.75:
                p.remove(p[i-1])
            else:

                i+=1
    
    #print(" ")
    #for p in newPara:
    #    print(p)

    output=open(output_name, 'w')
    for paras in newPara:
        if len(paras)>1:
            output.write('\n##' + " ".join(paras[0].common(paras[1]))+'\n')
        elif len(paras[0].keywords)>0:
            output.write('\n##' + paras[0].keywords[0]+'\n')
        for p in paras:
            if len(p.text)>5:
                output.write("\t"+p.text+"\n")
    output.close()

    #print(" ")
    #print(open("out.txt", 'r').read())




if __name__=='__main__':
    folder=sys.argv[1]

    compile(["../"+folder+"/notes.md", "new_notes.txt"], \
            "../"+folder+"/notes.md")



