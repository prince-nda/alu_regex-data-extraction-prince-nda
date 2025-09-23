import re

def extract_emails(text):
    """Extract email addresses from text"""
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

def extract_urls(text):
    """Extract URLs from text"""
    return re.findall(r'https?://[^\s"<>()]+', text)

def extract_credit_cards(text):
    """Extract credit card from text"""
    pattern = r'(?:\d{4}[- ]?){3}\d{4}\b'
    return re.findall(pattern, text)

def extract_times(text):
    """Extract 12-hour and 24 hour from text"""
    pattern_24 = r'\b(?:[01]?\d|2[0-3]):[0-5]\d\b(?!\s?(?:AM|PM|am|pm))'
    pattern_12 = r'\b(?:0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM|am|pm)\b'
    times_24 = re.findall(pattern_24, text)
    times_12 = re.findall(pattern_12, text)
    return times_24 + times_12

def extract_html_tags(text):
    """Extract HTML tags from text."""
    return re.findall(r'<[^>]+>', text)

if __name__ == "__main__":
    sample = """ 
    email:prince.nda@example.com james.nda@example.co.uk
    visit: https://www.example.com https://subdomain.example.org/page
    card:1234 5678 9012 3456, 1234-5678-9012-3456, 1234567890123567, 1234 5678 9013
    event time at 14:30 or 2:30 PM. and 08:25 am
    HTML: <p> <div class="example"> <img src="image.jpg" alt="description">
    """

    print("========== ALU REGEX DATA EXTRACTION =========\n")
    
    print("Emails:")
    for email in extract_emails(sample):
        print(" -", email)  
    print()
    
    print("URLs:")
    for url in extract_urls(sample):
        print(" -", url)
    print()
    
    print("Credit cards:")
    for card in extract_credit_cards(sample):
        print(" -", card)
    print()
    
    print("Times:")
    for t in extract_times(sample):
        print(" -", t)
    print()

    print("HTML tags:")
    for tag in extract_html_tags(sample):
        print(" -", tag)
