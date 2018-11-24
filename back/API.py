import requests
import json
import sys


headers={
    "X-Mashape-Key": "swb9S2ZELsmsh8SWVp7nMrUs2NxKp1ziuTxjsnEyYj69sVinYt",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  }

def getString(s1, s2):
    params={
        "text1": s1,
        "text2": s2
    }
    return requests.post('https://twinword-text-similarity-v1.p.mashape.com/similarity/', 
    params=params, headers=headers)
    

j=json.loads(getString("HEY", "HELLO").text)
print(j)
print(j['similarity'])

