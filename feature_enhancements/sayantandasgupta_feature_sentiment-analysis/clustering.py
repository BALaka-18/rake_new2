import numpy as np
import pandas as pd
from gensim.models import Word2Vec
from sklearn.cluster import KMeans

vectors = Word2Vec.load("word2vec.model").wv

cluster_model = KMeans(n_clusters=2, max_iter=1000, random_state=True, n_init=50).fit(
    vectors.vectors.astype("double")
)

vectors.similar_by_vector(
    cluster_model.cluster_centers_[1], topn=10, restrict_vocab=None
)

positive_cluster_centre = cluster_model.cluster_centers_[1]
negative_cluster_centre = cluster_model.cluster_centers_[0]

keywords = pd.DataFrame(vectors.vocab.keys())
keywords.columns = ["keywords"]
keywords["vectors"] = keywords.keywords.apply(lambda x: vectors[f"{x}"])
keywords["cluster"] = keywords.vectors.apply(
    lambda x: cluster_model.predict([np.array(x)])
)
keywords.cluster = keywords.cluster.apply(lambda x: x[0])

keywords["cluster_value"] = [1 if i == 1 else -1 for i in keywords.cluster]
keywords["closeness_score"] = keywords.apply(
    lambda x: 1 / (cluster_model.transform([x.vectors]).min()), axis=1
)
keywords["sentiment_coeff"] = keywords.closeness_score * keywords.cluster_value

keywords[["keywords", "sentiment_coeff"]].to_csv("sent_dictionary.csv", index=False)
