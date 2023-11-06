import requests
import os
from dotenv import load_dotenv
# Load variables from the .env file
load_dotenv()

# Function to fetch job postings from Indeed API
def fetch_job_postings(query):
    api_endpoint = "https://api.indeed.com/ads/apisearch"
    api_params = {
        'publisher': 'YOUR_PUBLISHER_ID',  # Replace with your Indeed publisher ID
        'q': query,
        'v': '2',
        'format': 'json'
    }

    response = requests.get(api_endpoint, params=api_params)
    return response.json()


# Access the environment variables
# indeed_publisher_key = os.getenv('INDEED_PUBLISHER_KEY')
adzuna_api_key = os.getenv('ADZUNA_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

# Use these variables in your code
# Example:
# api_key = indeed_publisher_key  # Use this in your API requests
