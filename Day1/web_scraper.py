import requests
import csv

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

# Download the input file
url_to_scrape = "https://adventofcode.com/2023/day/1/input"
session_cookie = "53616c7465645f5f7ba92079bad229ee4e0bb4183f1d0d83691aa75bb87ef295c734e88802ce1d48c32f77d29bd4ab3af54a74be9d9cdd74dcf31de2336d2155"

lines_of_text = download_input_file(url_to_scrape, session_cookie)

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