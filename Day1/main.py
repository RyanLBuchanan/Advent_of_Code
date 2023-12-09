from web_scraper import download_input_file

# Example usage:
url_to_scrape = "https://adventofcode.com/2023/day/1/input"
session_cookie = "53616c7465645f5f7ba92079bad229ee4e0bb4183f1d0d83691aa75bb87ef295c734e88802ce1d48c32f77d29bd4ab3af54a74be9d9cdd74dcf31de2336d2155"  # Replace with your actual session cookie

lines_of_text = download_input_file(url_to_scrape, session_cookie)

if lines_of_text:
    print(lines_of_text)
    # Now you can use the input_data as needed
else:
    print("Download failed. Please check the URL and session cookie.")
def sum_of_first_and_last_digit(lines):
    total_sum = 0

    for line in lines:
        # Find the first and last digit and convert them to integers
        digits = [int(char) for char in line if char.isdigit()]

        # Check if at least one digit was found in the line
        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]

            # Add the combination of the two digits as one integer to the total sum
            total_sum += (first_digit * 10 + last_digit)

            print(f"Line: {line}, Integer: {first_digit * 10 + last_digit}")

    return total_sum


# Example usage:
# lines_of_text = ["123", "456", "789"]
result = sum_of_first_and_last_digit(lines_of_text)
print(result)