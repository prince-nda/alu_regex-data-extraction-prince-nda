import re

def extract_emails(text):
    """Extract email addresses from text"""
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

def extract_urls(text):
    """Extract URLs from text"""
    return re.findall(r'https?://[^\s"<>()]+', text)

def extract_credit_cards(text):
    """Extract credit card from text"""
    pattern = r'(?:\d{4}[- ]?){3}\d{4}'
    return re.findall(pattern, text)

def extract_times(text):
    """Extract 12-hour and 24 hour from text"""
    pattern_24 = r'\b([01]?\d|2[0-3]):[0-5]\d\b'
    pattern_12 = r'\b([1-9]|1[0-2]):[0-5]\d\s?(AM|PM|am|pm)\b'
    times_24 = re.findall(pattern_24, text)
    times_12 = [''.join(match) for match in re.findall(pattern_12, text)]
    return times_24 + times_12

def extract_html_tags(text):
    """Extract HTML tags from text."""
    return re.findall(r'<[^>]+>', text)

if __name__ == "__main__":
    sample = """ 
    email:prince.nda@example.com james.nda@example.co.uk
    visit: https://www.example.com https://subdomain.example.org/page
    card:1234 5678 9012 3456 1234-5678-9012-3456
    event time at 14:30 or 2:30. Also at 09:15 am
    HTML: <p> <div class="example"> <img src="image.jpg" alt="description">
    """

    print("Emails:", extract_emails(sample))
    print("URLs:", extract_urls(sample))
    print("Credit cards:", extract_credit_cards(sample))
    print("Times:", extract_times(sample))
    print("HTML tags:", extract_html_tags(sample))
