import requests

subscription_key = "af57e3078bed417e99c36bf414aeb316"
assert subscription_key


text_analytics_base_url = "https://uksouth.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases"

key_phrase_api_url = text_analytics_base_url + "keyPhrases"
print(key_phrase_api_url)

documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
  {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
  {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
  {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
]}
headers   = {'Ocp-Apim-Subscription-Key': subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()
print(key_phrases)
