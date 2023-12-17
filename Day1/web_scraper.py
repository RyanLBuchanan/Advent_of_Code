import os
import requests
import csv

def download_input_file(url):
    try:
        # Retrieve the AOC_SESSION environment variable
        session_cookie = os.environ.get('AOC_SESSION')

        # Check if the session ID is available
        if session_cookie is None:
            print("AOC_SESSION environment variable not set. Please set it before running the script.")
            return None

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

# Download the input file
url_to_scrape = "https://adventofcode.com/2023/day/1/input"
lines_of_text = download_input_file(url_to_scrape)

# Check if download was successful
if lines_of_text:
    # Open a CSV file for writing
    with open("output.csv", "w") as csvfile:
        writer = csv.writer(csvfile)

        # Split lines and write to CSV
        for line in lines_of_text.strip().split(" "):
            writer.writerow([line])

        print("CSV file successfully created!")
else:
    print("Failed to download the input file.")
