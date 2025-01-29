class ExtractiveSummarizer:
    def __init__(self, text):
        self.text = text
        self.sentences = self._split_into_sentences(text)

    def _split_into_sentences(self, text):
        # Basic sentence splitting logic
        return text.split('. ')

    def summarize(self, num_sentences=3):
        # Simple extractive summarization by selecting the first few sentences
        return '. '.join(self.sentences[:num_sentences]) + '.'

    def rank_sentences(self):
        # Placeholder for ranking sentences based on importance
        pass

    def get_summary(self, num_sentences=3):
        ranked_sentences = self.rank_sentences()
        # Logic to select sentences based on ranking
        return self.summarize(num_sentences)