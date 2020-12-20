import re
from re import sub
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize

def text_preprocess(text):
    text = str(text)
    text = text.lower()

    stop_words = stopwords.words('english')

    #clean the text

    text = sub(r"[^A-Za-z0-9^,!?.\/'+]", " ",text)
    text = sub(r"\+","plus",text)
    text = sub(r","," ",text)
    text = sub(r"\.", " ", text)
    text = sub(r"!", " ! ", text)
    text = sub(r"\?", " ? ", text)
    text = sub(r"'", " ", text)
    text = sub(r":", " : ", text)
    text = sub(r"\s{2,}", " ", text)
    text = sub(r"\n","",text)
    text = word_tokenize(text)
    text = [word for word in text if word not in stop_words]

    return text

def file_preprocess():
    file1 = open(r"E:\big.txt","r")
    sent_list = file1.readlines()
    sent_list = [re.sub(r"\n"," ",x) for x in sent_list]

    #text = ""
    #for x in sent_list:
     #   text = text + x
    
    #sentences = sent_tokenize(text)

    word_vec = [text_preprocess(sent) for sent in sent_list]
    word_vec = [sent for sent in word_vec if len(sent)>0]
    return word_vec



vector = file_preprocess()

print(vector[0:5])
