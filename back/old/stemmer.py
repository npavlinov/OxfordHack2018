import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob, Word
from nltk.corpus import stopwords
from rake_nltk import Rake





def analyse(sentence):
##    r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
##    r.extract_keywords_from_text(sentence)
##    sentence=' '.join(r.get_ranked_phrases()) # To get keyword phrases ranked highest to lowest.


    
    nltk_tokens=[w.lemmatize() for w in TextBlob(sentence.lower()).words]

 
    lemmatized = list(filter(lambda word: word not in stopwords.words('english'), nltk_tokens))
    print(lemmatized)
##    porter_stemmer = PorterStemmer()
##    stemmezed=[]
##    for w in lemmatized:
##        stemmezed.append(porter_stemmer.stem(w))
##    #return stemmezed
##    #return ' '.join(stemmezed)

    r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
    r.extract_keywords_from_text(' '.join(lemmatized))
    return r.get_ranked_phrases() # To get keyword phrases ranked highest to lowest.


    return ' '.join(lemmatized)

if __name__=='__main__':
    print(analyse("""The hippocampus (named after its resemblance to \
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
    



   
