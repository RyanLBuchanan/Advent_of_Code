import requests

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

def sum_first_and_last_digits(lines):
    """
    Extracts the first and last digits from each line in a list of strings, converts them to integers, and returns their sum.

    Args:
        lines: A list of strings containing lines of text.

    Returns:
        The sum of the extracted digit combinations.
    """
    total_sum = 0

    for line in lines:
        # Extract first and last digits
        first_digit = line[0]
        last_digit = line[-1]

        # Check if both characters are digits
        if first_digit.isdigit() and last_digit.isdigit():
            # Convert digits to integers and add their combination to the total sum
            total_sum += int(first_digit) * 10 + int(last_digit)

    return total_sum

# Download the text
url_to_scrape = "https://adventofcode.com/2023/day/1/input"
session_cookie = "53616c7465645f5f7ba92079bad229ee4e0bb4183f1d0d83691aa75bb87ef295c734e88802ce1d48c32f77d29bd4ab3af54a74be9d9cdd74dcf31de2336d2155"

lines_of_text = download_input_file(url_to_scrape, session_cookie)

# Check if download was successful
if lines_of_text:
    # Process the text
    total_sum = sum_first_and_last_digits(lines_of_text.strip().split(" "))

    # Print the result
    print(f"Total sum: {total_sum}")
else:
    print("Failed to download the input file.")
