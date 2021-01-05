import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


def predict():
    final_file = pd.read_csv("final_dict.csv")
    final_file.head(10)

    final_file["sentiment_rate"] = final_file.apply(
        lambda x: np.array(x.loc["sentiment_coeff"]) * np.array(x.loc["TFIDF"]), axis=1
    )
    final_file["prediction"] = (final_file.sentiment_rate > 0).astype("int8")
    final_file["sentiment"] = [1 if i == 1 else 0 for i in final_file.sentiment_rate]

    final_file[["prediction", "sentiment"]].to_csv("predictions.csv")


predict()
