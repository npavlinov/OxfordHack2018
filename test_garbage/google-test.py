
# Open in Cloud Shell View on GitHub Feedback

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
#
# # Instantiates a client
# client = language.LanguageServiceClient()
#
# # The text to analyze
# text = u'Hello, world!'
# document = types.Document(
#     content=text,
#     type=enums.Document.Type.PLAIN_TEXT)
#
# # Detects the sentiment of the text
# sentiment = client.analyze_sentiment(document=document).document_sentiment
#
#
#
#
# print('Text: {}'.format(text))
# print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))


 # """Detects entities in the text."""
import six

text = "In Alzheimer's disease (and other forms of dementia), the hippocampus is \
one of the first regions of the brain to suffer damage; short-term memory loss \
and disorientation are included among the early symptoms. Damage to the \
hippocampus can also result from oxygen starvation (hypoxia), encephalitis, \
or medial temporal lobe epilepsy. People with extensive, bilateral hippocampal \
damage may experience anterograde amnesia (the inability to form and retain new \
memories)."
text= "The frontal lobe, located at the front of the brain, is the largest of the \
four major lobes of the cerebral cortex in mammals. The frontal lobe is located \
at the front of each cerebral hemisphere (in front of the parietal lobe and the \
temporal lobe). It is separated from the parietal lobe by a groove between tissues \
called the central sulcus, and from the temporal lobe by a deeper groove called \
the lateral sulcus (Sylvian fissure). The most anterior rounded part of the \
frontal lobe (though not well-defined) is known as the frontal pole, one of the \
three poles of the cerebrum."
text="The primary motor cortex (Brodmann area 4) is a brain region that in \
humans is located in the dorsal portion of the frontal lobe. It is the primary \
region of the motor system and works in association with other motor areas i\
ncluding premotor cortex, the supplementary motor area, posterior parietal cortex, \
and several subcortical brain regions, to plan and execute movements. Primary \
motor cortex is defined anatomically as the region of cortex that contains large \
neurons known as Betz cells. Betz cells, along with other cortical neurons, send \
long axons down the spinal cord to synapse onto the interneuron circuitry of \
the spinal cord and also directly onto the alpha motor neurons in the spinal \
cord which connect to the muscles."
client = language.LanguageServiceClient()
if isinstance(text, six.binary_type):
    text = text.decode('utf-8')

    # Instantiates a plain text document.
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
entities = client.analyze_entities(document).entities

    # entity types from enums.Entity.Type
entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
               'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

for entity in entities:
    print('=' * 20)
    print(u'{:<16}: {}'.format('name', entity.name))
    print(u'{:<16}: {}'.format('type', entity_type[entity.type]))
    print(u'{:<16}: {}'.format('metadata', entity.metadata))
    print(u'{:<16}: {}'.format('salience', entity.salience))
    print(u'{:<16}: {}'.format('wikipedia_url',
              entity.metadata.get('wikipedia_url', '-')))
