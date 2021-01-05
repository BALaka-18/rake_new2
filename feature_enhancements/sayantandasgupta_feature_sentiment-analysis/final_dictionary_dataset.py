import re
from re import sub
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


def file_preprocess():
    file1 = open(r"big.txt", "r")
    sent_list = file1.readlines()
    sent_list = [re.sub(r"\n", " ", x) for x in sent_list]
    return sent_list


def create_tfidf():
    dataset = file_preprocess()
    tfIdfVectorizer = TfidfVectorizer(use_idf=True)
    tfIdf = tfIdfVectorizer.fit_transform(dataset)
    df = pd.DataFrame(
        tfIdf[0].T.todense(),
        index=tfIdfVectorizer.get_feature_names(),
        columns=["TF-IDF"],
    )
    df = df.sort_values("TF-IDF", ascending=False)
    df.to_csv("tfidf_dict.csv", index=False)


create_tfidf()

sent_dict = pd.read_csv("sent_dictionary.csv")

df = pd.read_csv("tfidf_dict.csv")

sent_dict["TFIDF"] = [df["TF-IDF"].word for word in sent_dict.keywords]

sent_dict.head()

sent_dict.to_csv("final_dict.csv", index=False)
