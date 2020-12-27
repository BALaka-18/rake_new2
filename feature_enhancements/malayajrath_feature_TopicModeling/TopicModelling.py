def preprocessing(doc):
    import re
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    corpus=[]
    doc=doc.split()
    for i in range(len(doc)):
        text = re.sub('[^a-zA-Z]', ' ', doc[i])
        text = text.lower()
        text = text.split()
        all_stopwords = stopwords.words('english')
        all_stopwords.remove('not')
        text = [word for word in text if not word in set(all_stopwords)]
        text = ' '.join(text)
        corpus.append(text)
    corpus = list(filter(None, corpus))
    return corpus

def topic_modelling(preproc,n):
    from sklearn.feature_extraction.text import CountVectorizer
    cv=CountVectorizer(max_df=0.9,min_df=2,stop_words='english')
    dtm=cv.fit_transform(preproc)
    from sklearn.decomposition import LatentDirichletAllocation
    LDA=LatentDirichletAllocation(n_components=1,random_state=42)
    LDA.fit(dtm)
    Topics=[]
    for index,topic in enumerate(LDA.components_):
        Topics=[cv.get_feature_names()[i] for i in topic.argsort()[-n:]]
    return Topics


def main():
    doc = input()
    n = int(input("enter the no. of topics "))
    preproc = preprocessing(doc)
    topics = topic_modelling(preproc, n)
    for i in topics:
        print(i)

if __name__=='__main__':
    main()