from web_scraper import download_input_file

# Example usage:
url_to_scrape = "https://adventofcode.com/2023/day/1/input"
session_cookie = "53616c7465645f5f7ba92079bad229ee4e0bb4183f1d0d83691aa75bb87ef295c734e88802ce1d48c32f77d29bd4ab3af54a74be9d9cdd74dcf31de2336d2155"  # Replace with your actual session cookie

lines_of_text = download_input_file(url_to_scrape, session_cookie)

# if lines_of_text:
#     print(lines_of_text)
#     # Now you can use the input_data as needed
# else:
#     print("Download failed. Please check the URL and session cookie.")
# def sum_of_first_and_last_digit(lines):
#     total_sum = 0
#
#     for line in lines:
#         # Find the first and last digit and convert them to integers
#         digits = [int(char) for char in line if char.isdigit()]
#
#         # Check if at least one digit was found in the line
#         if digits:
#             first_digit = digits[0]
#             last_digit = digits[-1]
#
#             # Add the combination of the two digits as one integer to the total sum
#             total_sum += (first_digit * 10 + last_digit)
#
#             print(f"Line: {line}, Integer: {first_digit * 10 + last_digit}")
#
#     return total_sum


# Example usage:
# lines_of_text = ["123", "456", "789"]
# result = sum_of_first_and_last_digit(lines_of_text)
# print(result)


# import re
#
# def extract_digits(lines, index):
#   """
#   Extracts the first and last digits from a string at a given index.
#
#   Args:
#     text: The string to extract digits from.
#     index: The index of the digits to extract.
#
#   Returns:
#     A string containing the first and last digits, or an empty string if no digits are found.
#   """
#   total_sum = 0
#
#   for line in lines:
#
#     digits = re.findall(r"\d", lines)
#     if len(digits) >= index + 1:
#       return digits[index] + digits[-1]
#     else:
#       return ""
#
# # Example usage
# # text = "This string has 12345 digits."
# index = 0
#
# extracted_digits = extract_digits(lines_of_text, index)
#
# print(f"Extracted digits: {extracted_digits}")


import re

def sum_of_first_and_last_digit(lines):
  """
  Extracts and sums the first and last digits from each line in a list of strings, and prints the result for each line.

  Args:
    lines: A list of strings containing lines of text.

  Returns:
    The total sum of the extracted digit combinations.
  """
  total_sum = 0

  for line in lines:
    # Remove extra spaces and split into individual lines
    clean_line = line.strip().split(" ")

    for word in clean_line:
      # Extract first and last digits from each word
      extracted_digits = extract_digits(word, 0)

      # Check if digits were found
      if extracted_digits:
        # Convert digits to integers and add their combination to the total sum
        first_digit, last_digit = map(int, extracted_digits)
        individual_sum = first_digit * 10 + last_digit
        total_sum += individual_sum

        # Print information
        print(f"Line: '{word}', Integer: {individual_sum}")

  print(f"\nTotal sum: {total_sum}")

# Define function to extract digits
def extract_digits(text, index):
  """
  Extracts the first and last digits from a string at a given index.

  Args:
    text: The string to extract digits from.
    index: The index of the digits to extract.

  Returns:
    A string containing the first and last digits, or an empty string if no digits are found.
  """
  digits = re.findall(r"\d", text)
  if len(digits) >= index + 1:
    return digits[index] + digits[-1]
  else:
    return ""

# Example usage
lines = [
    "This string has 12345 digits.",
    "This string has 67890 digits.",
    "This string has no digits.",
]

sum_of_first_and_last_digit(lines_of_text)
