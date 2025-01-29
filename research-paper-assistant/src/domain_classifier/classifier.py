from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

class DomainClassifier:
    def __init__(self, text: str):
        self.text = text
        self.model_path = "models/domain_classifier.pkl"
        self.vectorizer_path = "models/tfidf_vectorizer.pkl"
        self.model = joblib.load(self.model_path)
        self.vectorizer = joblib.load(self.vectorizer_path)

    def classify(self) -> str:
        X = self.vectorizer.transform([self.text])
        prediction = self.model.predict(X)
        return prediction[0]