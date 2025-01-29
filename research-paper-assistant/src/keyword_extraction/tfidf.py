class KeywordExtractor:
    def __init__(self, documents):
        self.documents = documents

    def compute_tfidf(self):
        from sklearn.feature_extraction.text import TfidfVectorizer
        
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(self.documents)
        return tfidf_matrix, vectorizer.get_feature_names_out()

    def extract_keywords(self, n_keywords=5):
        tfidf_matrix, feature_names = self.compute_tfidf()
        keywords = []

        for i in range(tfidf_matrix.shape[0]):
            sorted_indices = tfidf_matrix[i].toarray()[0].argsort()[::-1]
            top_keywords = [feature_names[idx] for idx in sorted_indices[:n_keywords]]
            keywords.append(top_keywords)

        return keywords