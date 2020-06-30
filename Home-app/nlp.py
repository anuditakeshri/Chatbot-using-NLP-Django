import nltk
import numpy
import random
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def lemmatization(tokens):
    lemmer = nltk.stem.WordNetLemmatizer()
    return[lemmer.lemmatize(token) for token in tokens]


def normalize(text):
    remove_punct = dict((ord(punct),None) for punct in string.punctuation)
    return lemmatization(nltk.word_tokenize(text.lower().translate(remove_punct)))



def greeting(sentence):
    for word in sentence.split(" "):
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)



def find_response(response):
    chatbots_file = open('E:\\NLP_Project\\Chatbot\\templates\\info.txt','r',errors = 'ignore')
    info_data = chatbots_file.read()
    info_data = info_data.lower()
    nltk.download('punkt')
    nltk.download('wordnet')
    sentence_tokens = nltk.sent_tokenize(info_data)
    word_tokens = nltk.word_tokenize(info_data)
    
    
    bot_response = ''
    sentence_tokens.append(response)
    TfidfVec = TfidfVectorizer(tokenizer = normalize, stop_words = 'english')
    tfidf = TfidfVec.fit_transform(sentence_tokens)
    
    values = cosine_similarity(tfidf[-1],tfidf)
    idx = values.argsort()[0][-2]
    flat = values.flatten()
    flat.sort()
    
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        bot_response = bot_response + "I am sorry! I don't understand you"
    else:
        bot_response = bot_response + sentence_tokens[idx]
    return bot_response
 
    
remove_punct = {}    
GREETING_INPUTS = ("hello","hi","what's up","sup","hey")
GREETING_RESPONSES = ("hi","hey","hi there","hello","I am glad! You are talking to me")

def give_response(input_given): 
    input_given = input_given.lower()
    if(input_given!='bye'):
        if(input_given=='thanks' or input_given=='thank you'):
            flag = False
            return('You are welcome!')
        else:
            if(greeting(input_given)!=None):
                return greeting(input_given)
            else:

                return find_response(input_given)
                sentence_tokens.remove(input_given)
    else:
        flag = False
        return ('Bye!')
