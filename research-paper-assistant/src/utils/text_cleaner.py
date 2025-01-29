def clean_text(text):
    """
    Cleans the input text by removing unwanted characters and formatting it.
    
    Parameters:
    text (str): The text to be cleaned.
    
    Returns:
    str: The cleaned text.
    """
    # Remove unwanted characters
    cleaned_text = ''.join(char for char in text if char.isalnum() or char.isspace())
    
    # Normalize whitespace
    cleaned_text = ' '.join(cleaned_text.split())
    
    return cleaned_text

def remove_special_characters(text):
    """
    Removes special characters from the input text.
    
    Parameters:
    text (str): The text to be processed.
    
    Returns:
    str: The text without special characters.
    """
    return clean_text(text)