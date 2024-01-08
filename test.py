import os
import requests
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Retrieve API key from .env file
api_key = os.getenv('GOOGLE_AI_KEY')

# Set the API URL
url = "https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText"

# Define the headers
headers = {
    'Content-Type': 'application/json',
}

# Define the data payload
data = {
    "prompt": {
        "text": "Write a story about a magic backpack"
    }
}

# Send the POST request
response = requests.post(url + "?key=" + api_key, json=data, headers=headers)

# Print the response
print(response.text)
