########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '954d23ee2b0243dca92c2ad1e7605e8f',
}

params = urllib.urlencode({
})

body = {
  "documents": [
        {
            "language": "en",
            "id": "1",
            "text": "In Alzheimer's disease (and other forms of dementia), the \
            hippocampus is one of the first regions of the brain to suffer damage; \
            short-term memory loss and disorientation are included among the early\
             symptoms. Damage to the hippocampus can also result from oxygen starvation \
             (hypoxia), encephalitis, or medial temporal lobe epilepsy. People with extensive, \
             bilateral hippocampal damage may experience anterograde amnesia (the \
             inability to form and retain new memories)."
        },
        {
            "language": "en",
            "id": "2",
            "text": "Final document. Calling Cognitive API again."
        }
    ]
}


try:
    conn = httplib.HTTPSConnection('uksouth.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
