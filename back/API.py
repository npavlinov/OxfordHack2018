import requests
import json
import sys


headers={
    "X-Mashape-Key": "swb9S2ZELsmsh8SWVp7nMrUs2NxKp1ziuTxjsnEyYj69sVinYt",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  }


params={
    "text1": str(text1),
    "text2": str(text2)
    }


r = requests.post('https://twinword-text-similarity-v1.p.mas\
hape.com/similarity/', params=params, headers=headers)

j=json.loads(r.text)
print(j)
print(j['similarity'])

