#!/usr/bin/env python

# Copyright 2016 Google, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This application demonstrates how to perform basic operations with the
Google Cloud Natural Language API
For more information, the documentation at
https://cloud.google.com/natural-language/docs.
"""

import argparse
import sys

from google-cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six



# [START language_entities_text]
def entities_text(text):
    """Detects entities in the text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    # [START language_python_migration_entities_text]
    # [START language_python_migration_document_text]
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    # [END language_python_migration_document_text]

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities

    for entity in entities:
        entity_type = enums.Entity.Type(entity.type)
        print('=' * 20)
        print(u'{:<16}: {}'.format('name', entity.name))
        print(u'{:<16}: {}'.format('type', entity_type.name))
        print(u'{:<16}: {}'.format('metadata', entity.metadata))
        print(u'{:<16}: {}'.format('salience', entity.salience))
        print(u'{:<16}: {}'.format('wikipedia_url',
              entity.metadata.get('wikipedia_url', '-')))
    # [END language_python_migration_entities_text]
# [END language_entities_text]



if __name__=='__main__':
    print(entities_text("""The hippocampus (named after its resemblance to \
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


    
