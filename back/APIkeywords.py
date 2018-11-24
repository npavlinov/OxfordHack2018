import requests
import json
import sys
from rake_nltk import Rake
import nltk
from nltk.corpus import stopwords

headers={
    "X-Mashape-Key": "swb9S2ZELsmsh8SWVp7nMrUs2NxKp1ziuTxjsnEyYj69sVinYt",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  }

def getString(s1):
    params={
        "text": s1,
    }
    return requests.post('https://twinword-topic-tagging.p.mashape.com/generate/', 
    params=params, headers=headers)
    
def getkeyAPI(s):
    return json.loads(getString(s).text)['keyword']

def getkey(s):
    r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
    r.extract_keywords_from_text(s.lower())
    keywords=r.get_ranked_phrases()
    new=[]
    for keys in keywords:
        words=nltk.word_tokenize(keys)
        calc=nltk.pos_tag(words)
        dic={}
        for i in range(len(calc)):
            dic[calc[i][0]]=calc[i][1]
        ch=''
        for w in words:
            if dic[w]=='VB' or dic[w]=='MD':
                if ch!='':
                    while ch[-1]==' ':
                        try:
                            print(pos_tag(ch))
                        except:
                            pass
                        ch=ch[:-1]
                    new.append(ch)
                ch=''
            else:
                ch+=w.replace(')', '').replace('.', '').replace(',', '')
                ch+=' '
        if ch!='':
            while ch[-1]==' ':
                ch=ch[:-1]
            new.append(ch)
        ch=''
        
    print(new)
    newnew = list(filter(lambda word: word not in \
                             stopwords.words('english'), new))
    print(newnew)

                
        
        

    
if __name__=='__main__':
    print(getkey("""The hippocampus (named after its resemblance to \
the seahorse, from the Greek , "seahorse" from hippos, "horse" and kampos, \
"sea monster") is a major component of the brains of humans and other \
vertebrates. Humans and other mammals have two hippocampi, one in each \
side of the brain. The hippocampus belongs to the limbic system and plays \
important roles in the consolidation of information from short-term memory \
to long-term memory, and in spatial memory that enables navigation. The \
hippocampus is located under the cerebral cortex (allocortical) and in \
primates in the medial temporal lobe. It contains two main interlocking \
parts: the hippocampus proper (also called Ammon's horn) and the dentate \
gyrus. """))
    print()
    print(getkey("""In Alzheimer's disease, the hippocampus is one of the first \
regions of the brain to suffer damage; short-term memory loss and \
disorientation are included among the early symptoms. Damage to the \
hippocampus can also result from oxygen starvation, encephalitis, or \
medial temporal lobe epilepsy. People with extensive, bilateral \
hippocampal damage may experience anterograde amnesia."""))
    print()
    print(getkey("""The frontal lobe, located at the front of the brain, is \
the largest of the major lobes of the cerebral cortex in mammals. \
The frontal lobe is located at the front of each cerebral hemisphere (in \
front of the parietal lobe and the temporal lobe). It is separated from \
the parietal lobe by a groove between tissues called the central sulcus, \
and from the temporal lobe by a deeper groove called the lateral sulcus \
(Sylvian fissure). The most anterior rounded part of the frontal lobe \
(though not well-defined) is known as the frontal pole, one of the three \
poles of the cerebrum."""))
    print()
    print(getkey("""The precentral gyrus, a portion of the frontal lobe directly \
anterior to the central sulcus, contains the primary motor cortex, which \
controls voluntary movements of specific body parts."""))

