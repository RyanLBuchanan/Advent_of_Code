import requests
from bs4 import BeautifulSoup

# Set your Advent of Code session ID
session_id = "53616c7465645f5fc24dfcced561e69cc93a26e453da7dde59effcc921c8cc62c443571412c55b7df1f36d0adf4e58a5d8696ec3e7eb9ddd47c2689dd2fb937c"

# Function to extract digits from a line, handling both numeric and spelled-out digits
def extract_digits(line):
    digit_mapping = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }

    current_digits = ""
    result = 0

    # Iterate through the characters in the line
    for char in line:
        if char.isdigit():
            current_digits += char
        elif char.isalpha():
            # Check if spelled-out digit is found
            spelled_out_digit = ""
            while char.isalpha():
                spelled_out_digit += char
                char = next(iter(line), None)

            # Convert spelled-out digit to actual digit using the dictionary
            digit_value = digit_mapping.get(spelled_out_digit.lower(), None)
            if digit_value is not None:
                current_digits += str(digit_value)

    # Convert the accumulated digits to an integer
    result = int(current_digits) if current_digits else 0

    return result

# URL to scrape
url_to_scrape = "https://adventofcode.com/2023/day/1/input"

# Send a GET request with the session cookie
response = requests.get(url_to_scrape, cookies={'session': session_id})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract the lines of text
    lines = [line.get_text() for line in soup.find_all('pre')]

    # Print the URL being processed
    print(f"Processing URL: {url_to_scrape}")

    # Iterate through each line of text
    for i, line in enumerate(lines, start=1):
        # Print the current line being processed
        print(f"Line {i}: {line}")

    # Extracted digits from each line
    extracted_digits = [extract_digits(line) for line in lines]

    # Sum of extracted digits
    total_sum = sum(extracted_digits)

    # Print the total sum
    print(f"Total Sum: {total_sum}")

else:
    print(f"Failed to retrieve content. Status code: {response.status_code}")
