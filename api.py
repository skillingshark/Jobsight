import requests
import os

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('WORKABLE_API_KEY')

def fetch_jobs():
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get('https://www.workable.com/spi/v3/accounts/{account_id}/jobs', headers=headers)
    jobs = response.json()['jobs']
    return jobs
