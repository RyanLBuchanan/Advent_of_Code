import pandas as pd
import requests
import os


def download_input_file(url, session_cookie):
    try:
        # Use a session to maintain login state
        with requests.Session() as session:
            cookies = {'session': session_cookie}
            response = session.get(url, cookies=cookies)

            # Check if the request was successful
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to retrieve content. Status code: {response.status_code}")
                return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def sum_first_and_last_digits(csv_file):
    """
    Extracts the first and last digits from each line in a CSV file, converts them to integers, and returns their sum.

    Args:
        csv_file: Path to the CSV file.

    Returns:
        The sum of the extracted digit combinations.
    """
    total_sum = 0
    counter = 0

    # Read the CSV file using pandas
    with open(csv_file, "r") as file:
        data = pd.read_csv(file, header=None)

    # Extract first and last digits from each line
    for line in data.iloc[:, 0]:
        first_digit = None
        last_digit = None

        # Iterate through the characters in the line to find the first digit
        for char in line:
            if char.isdigit():
                first_digit = char
                break  # Exit the loop once the first digit is found

        # Iterate through the characters in reverse to find the last digit
        for char in reversed(line):
            if char.isdigit():
                last_digit = char
                break  # Exit the loop once the last digit is found

        # Check if both first and last digits are found
        if first_digit is not None and last_digit is not None:
            # Convert digits to integers and add their combination to the total sum
            individual_sum = int(first_digit) * 10 + int(last_digit)
            total_sum += individual_sum

            # Print information
            print(f"Line {counter}: '{line}', Integer: {individual_sum}")

            counter += 1

    return total_sum

# Download the input file
url_to_scrape = "https://adventofcode.com/2023/day/1/input"
session_cookie = "53616c7465645f5f7ba92079bad229ee4e0bb4183f1d0d83691aa75bb87ef295c734e88802ce1d48c32f77d29bd4ab3af54a74be9d9cdd74dcf31de2336d2155"

lines_of_text = download_input_file(url_to_scrape, session_cookie)

# Save the downloaded text to a temporary CSV file
if lines_of_text:
    with open("temp.csv", "w") as file:
        file.write(lines_of_text)

    # Calculate the sum using the CSV file
    total_sum = sum_first_and_last_digits("temp.csv")

    print(f"Total sum: {total_sum}")

    # Delete the temporary CSV file
    os.remove("temp.csv")
else:
    print("Failed to download the input file.")
