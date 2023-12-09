import requests

def download_input_file(url, session_cookie):
    try:
        # Use a session to maintain login state (replace 'your_session_cookie' with your actual session cookie)
        with requests.Session() as session:
            cookies = {'session': session_cookie}
            response = session.get(url, cookies=cookies)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to retrieve content. Status code: {response.status_code}")
                return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
