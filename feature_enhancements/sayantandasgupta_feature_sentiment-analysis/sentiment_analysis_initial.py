from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()

    score = analyzer.polarity_scores(text)

    if score["pos"] * 100 > 50:
        print("Positive : " + str(score["pos"] * 100) + "%")

    elif score["neg"] * 100 > 50:
        print("Negative : " + str(score["neg"] * 100) + "%")

    elif score["neu"] * 100 > 50:
        print("Neutral : " + str(score["neu"] * 100) + "%")


analyze_sentiment("I love the food here!")
