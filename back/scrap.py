from bs4 import BeautifulSoup
import requests


def get_from_url(url, maxi=-2):
    r=requests.get(url)
    html_doc=r.text
    soup = BeautifulSoup(html_doc, "html5lib")

    page = ''
    ##scrape all to maxi
    if maxi>=0:
        for p in soup.find_all('p')[:maxi]:
            txt=p.text+'\n'
            b=txt.find('[')
            while b!=-1:
                e=txt.find(']', b)
                txt=txt[:b]+txt[e:]
                b=txt.find('[')
            page+=txt
    #scrape all
    elif maxi==-1:
        for p in soup.find_all('p'):
            txt=p.text+'\n'
            b=txt.find('[')
            while b!=-1:
                e=txt.find(']', b)
                txt=txt[:b]+txt[e:]
                b=txt.find('[')
            page+=txt
    ##scrape only the introduction paragraphes, in a wikipedia type web page
    elif maxi==-2:
        for p in soup.find("div", { "id" : "toc" }).find_previous_siblings('p'):
            txt=p.text+'\n'
            b=txt.find('[')
            while b!=-1:
                e=txt.find(']', b)
                txt=txt[:b]+txt[e:]
                b=txt.find('[')
            page+=txt
    return page


if __name__=='__main__':
    URL = "https://en.wikipedia.org/wiki/Hippocampus"

    print(get_from_url(URL, -2))



