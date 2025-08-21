import re

def extract_dates(text):
    """
    Extracts all dates in DD-MM-YYYY or DD/MM/YYYY format from text.
    """
    pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(pattern, text)

# Example
sample_text = "Important dates: 17-08-2025, 25/12/2024, and 01-01-2026."
print("Extracted dates:", extract_dates(sample_text))
