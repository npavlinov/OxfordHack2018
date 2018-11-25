
# Open in Cloud Shell View on GitHub Feedback

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import six

text1 = "In Alzheimer's disease (and other forms of dementia), the hippocampus is \
one of the first regions of the brain to suffer damage; short-term memory loss \
and disorientation are included among the early symptoms. Damage to the \
hippocampus can also result from oxygen starvation (hypoxia), encephalitis, \
or medial temporal lobe epilepsy. People with extensive, bilateral hippocampal \
damage may experience anterograde amnesia (the inability to form and retain new \
memories)."
text2 = "In rodents as model organisms, the hippocampus has been studied \
extensively as part of a brain system responsible for spatial memory and \
navigation. Many neurons in the rat and mouse hippocampus respond as place cells: \
that is, they fire bursts of action potentials when the animal passes through a \
specific part of its environment. Hippocampal place cells interact extensively \
with head direction cells, whose activity acts as an inertial compass, and \
conjecturally with grid cells in the neighboring entorhinal cortex."
text3 = "The hippocampus (named after its resemblance to the seahorse, from the \
Greek, seahorse from hippos, horse and, kampos, sea monster) is a major \
component of the brains of humans and other vertebrates. Humans and other \
mammals have two hippocampi, one in each side of the brain. The hippocampus \
belongs to the limbic system and plays important roles in the consolidation \
of information from short-term memory to long-term memory, and in spatial \
memory that enables navigation. "

def ent_detect(text):
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
    return entities,entity_type

entities, entity_type = ent_detect(text3)

for i in range(0,3):
    print('=' * 20)
    print(u'{:<16}: {}'.format('name', entities[i].name))
    print(u'{:<16}: {}'.format('metadata', entities[i].metadata))
    print(u'{:<16}: {}'.format('salience', entities[i].salience))
    print(u'{:<16}: {}'.format('wikipedia_url',
              entities[i].metadata.get('wikipedia_url', '-')))
