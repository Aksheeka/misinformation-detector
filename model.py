from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

headlines = [
    "Scientists discover new planet",
    "Government releases economic report",
    "Shocking secret doctors don't want you to know",
    "Miracle cure exposed by insiders",
    "Researchers publish climate study",
    "Breaking hidden truth about vaccines revealed"
]

labels = [0,0,1,1,0,1]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(headlines)

model = LogisticRegression()
model.fit(X, labels)

sensational_words = [
    "shocking",
    "secret",
    "exposed",
    "breaking",
    "miracle",
    "hidden truth"
]

def analyze_text(text):

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    text_lower = text.lower()

    sensational_count = 0
    for word in sensational_words:
        if word in text_lower:
            sensational_count += 1

    X_test = vectorizer.transform([text])
    prediction = model.predict(X_test)[0]

    score = sensational_count

    if abs(sentiment) > 0.6:
        score += 1

    if prediction == 1:
        score += 1

    if score >= 3:
        result = "High Risk of Misinformation"
    elif score == 2:
        result = "Moderate Risk"
    else:
        result = "Low Risk"

    return {
        "sentiment": round(sentiment,2),
        "sensational_words": sensational_count,
        "risk": result
    }