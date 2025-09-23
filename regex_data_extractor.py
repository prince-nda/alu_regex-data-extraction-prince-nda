#!/usr/bin/env python3
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

def print_matches(title, matches):
    print(f"{title}:")
    if matches:
        for m in matches:
            print(" -", m)
    else:
        print(" - No valid entry found")
    print()

if __name__ == "__main__":
    sample = """ 
    email:prince.nda@example.com james.nda@example.co.uk
    visit: https://www.example.com https://subdomain.example.org/page
    card:1234 5678 9012 3456, 1234-5678-9012-3456, 1234567890123567, 1234 5678 9013
    event time at 14:30 or 2:30 PM. and 08:25 am
    HTML: <p> <div class="example"> <img src="image.jpg" alt="description">
    """

    print("========== ALU REGEX DATA EXTRACTION =========\n")
    
    print("sample text validation\n")
    print_matches("Emails", extract_emails(sample))
    print_matches("URLs", extract_urls(sample))
    print_matches("Credit Cards", extract_credit_cards(sample))
    print_matches("Times", extract_times(sample))
    print_matches("HTML Tags", extract_html_tags(sample))
    
    print("\n------------------------------------\n")
    
    user_input = input("Enter your text to validate: ")
    print("== User Input Validation ==\n")
    print_matches("Emails", extract_emails(user_input))
    print_matches("URLs", extract_urls(user_input))
    print_matches("Credit Cards", extract_credit_cards(user_input))
    print_matches("Times", extract_times(user_input))
    print_matches("HTML Tags", extract_html_tags(user_input))
 

