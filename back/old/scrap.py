from bs4 import BeautifulSoup
import requests

URL = "https://en.wikipedia.org/wiki/Hippocampus"

r=requests.get(URL)

html_doc=r.text

soup = BeautifulSoup(html_doc, "html5lib")
    
for p in soup.find_all('p')[:3]:
    txt=p.text
    b=txt.find('[')
    while b!=-1:
        e=txt.find(']', b)
        txt=txt[:b]+txt[e:]
        b=txt.find('[')
    print(txt)

