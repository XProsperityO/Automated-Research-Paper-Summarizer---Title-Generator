def tokenize(text):
    """Tokenizes the input text into words."""
    return text.split()

def normalize(tokens):
    """Normalizes the tokens by converting them to lowercase."""
    return [token.lower() for token in tokens]

def preprocess_text(text):
    """Preprocesses the input text by tokenizing and normalizing."""
    tokens = tokenize(text)
    normalized_tokens = normalize(tokens)
    return normalized_tokens