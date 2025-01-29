class AbstractiveSummarizer:
    def __init__(self, model):
        self.model = model

    def generate_summary(self, text):
        # Implement the logic for generating a summary using the language model
        summary = self.model.generate(text)
        return summary

    def fine_tune_model(self, training_data):
        # Implement the logic for fine-tuning the model on the training data
        self.model.train(training_data)