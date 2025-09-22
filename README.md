# alu_regex-data-extraction-prince-nda

## Overview
This project extracts 5 common data types from text using Python regular expressions:

- Email addresses
- URLs
- Credit card numbers
- Time (12-hour & 24-hour formats)
- HTML tags

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/prince-nda/alu_regex-data-extraction-prince-nda.git
   cd alu_regex-data-extraction-prince-nda
   ```

2. **Run the extractor:**
   ```bash
   python3 extractor.py
   ```

   You can also test with your own text by editing `sample` in `extractor.py` or using `test_cases.txt`.

## Files

- `extractor.py` — Main Python script for data extraction.
- `test_cases.txt` — Sample input for testing all extractors.
- `README.md` — Project documentation and instructions.

## Functions

- `extract_emails`: Finds email addresses.
- `extract_urls`: Finds URLs.
- `extract_credit_cards`: Finds credit card numbers.
- `extract_times`: Finds times in 12/24-hour format.
- `extract_html_tags`: Finds HTML tags.

## Edge-case Handling

- Each regex is designed to catch common variations and edge cases (multiple formats, optional spaces/hyphens, etc.).
- You can expand `test_cases.txt` to test additional edge cases.

## Output Presentation

Running the script prints all extracted data types clearly labeled.

## Author

Prince NDAHIRO
