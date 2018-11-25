import requests
import json

def similarity(text1, text2):
    headers={
        "X-Mashape-Key": "swb9S2ZELsmsh8SWVp7nMrUs2NxKp1ziuTxjsnEyYj69sVinYt",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
      }
    params={
        "text1": text1,
        "text2": text2
        }
    r = requests.post('https://twinword-text-similarity-v1.p.mas\
    hape.com/similarity/', params=params, headers=headers)
    j=json.loads(r.text)
    return j['similarity']


if __name__=='__main__':
    similarity("The hippocampus is a major component of the brains of humans and \
other vertebrates. It belongs to the limbic system and plays important roles \
in the consolidation of information from short-term memory to long-term memory \
and spatial navigation. Humans and other mammals have two hippocampi, one in \
each side of the brain. The hippocampus is a part of the cerebral cortex; \
and in primates it is located in the medial temporal lobe, underneath the \
cortical surface. It contains two main interlocking parts: Ammon's horn \
and the dentate gyrus.", "An important part of the brains of humans and other vertebrates \
is the hippocampus. It's part of the limbic system and moves information from \
short-term to long-term memory. It also helps us move around. Humans and other \
mammals have two hippocampi, one on each side. The hippocampus is a part of \
the cerebral cortex; and in primates it is found in the medial temporal lobe, \
beneathe the cortical surface. It has two main interlocking parts: Ammon's \
horn and the dentate gyrus.")
