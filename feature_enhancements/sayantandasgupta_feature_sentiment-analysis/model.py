import multiprocessing
import re
from re import sub

import nltk
import pandas as pd
from gensim.models import Word2Vec
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


def text_preprocess(text):
    text = str(text)
    text = text.lower()

    stop_words = stopwords.words("english")

    # clean the text

    text = sub(r"[^A-Za-z0-9^,!?.\/'+]", " ", text)
    text = sub(r"\+", "plus", text)
    text = sub(r",", " ", text)
    text = sub(r"\.", " ", text)
    text = sub(r"!", " ! ", text)
    text = sub(r"\?", " ? ", text)
    text = sub(r"'", " ", text)
    text = sub(r":", " : ", text)
    text = sub(r"\s{2,}", " ", text)
    text = sub(r"\n", "", text)
    text = word_tokenize(text)
    text = [word for word in text if word not in stop_words]

    return text


def file_preprocess():
    file1 = open(r"E:\big.txt", "r")
    sent_list = file1.readlines()
    sent_list = [re.sub(r"\n", " ", x) for x in sent_list]

    word_vec = [text_preprocess(sent) for sent in sent_list]
    word_vec = [sent for sent in word_vec if len(sent) > 0]
    return word_vec


def build_model():

    word_vector = file_preprocess()

    cores = multiprocessing.cpu_count()

    model = Word2Vec(
        min_count=20,
        window=2,
        size=300,
        sample=6e-5,
        alpha=0.03,
        min_alpha=0.0007,
        negative=20,
        workers=cores - 1,
    )

    model.build_vocab(word_vector, progress_per=10000)

    model.train(word_vector,
                total_examples=model.corpus_count,
                epochs=30,
                report_delay=1)

    model.init_sims(replace=True)

    model.save("word2vec.model")


build_model()
