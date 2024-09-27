import os
import platform
import requests
from datetime import datetime
from dateutil import parser

def fetch_pakistan_time():
    """Fetch current time for Pakistan from an online API."""
    try:
        response = requests.get("http://worldtimeapi.org/api/timezone/Asia/Karachi")
        if response.status_code == 200:
            data = response.json()
            datetime_str = data['datetime']
            return parser.isoparse(datetime_str)  # Parse ISO 8601 format with timezone
        else:
            print("Failed to fetch time data from the API.")
            return None
    except Exception as e:
        print(f"An error occurred while fetching time: {e}")
        return None

def set_system_time(current_time):
    """Set the system time based on the current_time passed."""
    try:
        # Format time and date
        formatted_time = current_time.strftime('%H:%M:%S')
        formatted_date = current_time.strftime('%d-%m-%y')

        # Identify the operating system
        os_type = platform.system()

        # Set the time and date according to the OS
        if os_type == 'Windows':
            os.system(f'date {formatted_date}')
            os.system(f'time {formatted_time}')
        elif os_type == 'Linux':
            os.system(f'sudo date --set="{formatted_time}"')
            os.system(f'sudo date --set="{formatted_date}"')
        else:
            print(f"Unsupported OS: {os_type}")
    except Exception as e:
        print(f"An error occurred while setting the system time: {e}")

if __name__ == "__main__":
    # Fetch the current time
    pakistan_time = fetch_pakistan_time()

    # If time is successfully fetched, set the system time
    if pakistan_time:
        print(f"Fetched Pakistan Time: {pakistan_time}")
        set_system_time(pakistan_time)
    else:
        print("Could not fetch the time, exiting.")
