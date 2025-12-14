from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize once (important for performance)
sia = SentimentIntensityAnalyzer()


def analyze_sentiment(text: str) -> str:
    """
    Analyze sentiment of a text using VADER.
    Suitable for short user comments.
    """

    if not text or len(text.strip()) < 3:
        return "Neutral"

    scores = sia.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"
