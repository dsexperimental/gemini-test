import os
import requests
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Retrieve API key from .env file
api_key = os.getenv('GOOGLE_AI_KEY')

# Set the API URL
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

# Define the headers
headers = {
    'Content-Type': 'application/json',
}

# Define the data payload
data1 = {
    "contents": [
        {
            "parts": [
                {
                    "text": """You are a helpful AI assistant. In the following messages I will
                    give some example inputs and outputs. Then I will give you an input and
                    you try to get the right pattern for the outout. If you are ready to start,
                    respond "OK"
                    """
                }
            ],
            "role": "user"
        },
        {
            "parts": [
                {
                    "text": "OK"
                }
            ],
            "role": "model"
        },
        {
            "parts":[
                {
                    "text": "Jump"
                }
            ],
            "role": "user"
        },
        {
            "parts":[
                {
                    "text": "How high?"
                }
            ],
            "role": "model"
        },
        {
            "parts":[
                {
                    "text": "Run"
                }
            ],
            "role": "user"
        },
        {
            "parts":[
                {
                    "text": "How fast?"
                }
            ],
            "role": "model"
        },
        {
            "parts":[
                {
                    "text": "Yell"
                }
            ],
            "role": "user"
        }
    ]
}

data2 = {
    "contents": [
        {
            "parts":[
                {
                    "text": "What is 3 + 4, using the add tool?"
                }
            ],
            "role": "user"
        }
    ],
    "tools": [
        {
            "function_declarations": [
                {
                    "name": "add",
                    "description": "Add two numbers together.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "input1": {
                                "type": "number",
                            },
                            "input2": {
                                "type": "number",
                            }
                        },
                        "required": ["input1","input2"]
                    }
                }
            ]
        }
    ]
}


data3 = {
    "contents": [
        {
            "parts":[
                {
                    "text": "What is 3 + 4, using the add tool?"
                }
            ],
            "role": "user"
        },
        {
            "parts": [
                {
                    "functionCall": {
                    "name": "add",
                        "args": {
                            "input1": 3,
                            "input2": 4
                        }
                    }   
                }
            ],
            "role": "model"
        },
        {
            "parts": [
                {
                    "functionResponse": {
                        "name": "add",
                        "response": {
                            "name": "add",
                            "content": {
                                "text": "3 + 4 = 7"
                            }
                        }
                    }
                }
            ],
            "role": "function"
        }
    ],
    "tools": [
        {
            "function_declarations": [
                {
                    "name": "add",
                    "description": "Add two numbers together.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "input1": {
                                "type": "number",
                            },
                            "input2": {
                                "type": "number",
                            }
                        },
                        "required": ["input1","input2"]
                    }
                }
            ]
        }
    ]
}


# Send the POST request
response = requests.post(url + "?key=" + api_key, json=data1, headers=headers)

# Print the response
print(response.text)

#################

token_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:countTokens"

token_data1 = {
    "contents": [
        {
            "parts": [
                {
                    "text": """You are a helpful AI assistant. In the following messages I will
                    give some example inputs and outputs. Then I will give you an input and
                    you try to get the right pattern for the outout. If you are ready to start,
                    respond "OK"
                    """
                }
            ],
            "role": "user"
        },
        {
            "parts": [
                {
                    "text": "OK"
                }
            ],
            "role": "model"
        },
        {
            "parts":[
                {
                    "text": "Jump"
                }
            ],
            "role": "user"
        },
        {
            "parts":[
                {
                    "text": "How high?"
                }
            ],
            "role": "model"
        },
        {
            "parts":[
                {
                    "text": "Run"
                }
            ],
            "role": "user"
        },
        {
            "parts":[
                {
                    "text": "How fast?"
                }
            ],
            "role": "model"
        },
        {
            "parts":[
                {
                    "text": "Yell"
                }
            ],
            "role": "user"
        }
    ]
}



token_data2_1 = {
    "contents": [
        {
            "parts":[
                {
                    "text": "What is 3 + 4, using the add tool?"
                }
            ],
            "role": "user"
        }
    ]
}

token_data2_2 = {
    "contents": [
        {
            "parts": [
                {
                    "functionCall": {
                    "name": "add",
                        "args": {
                            "input1": 3,
                            "input2": 4
                        }
                    }   
                }
            ],
            "role": "model"
        }
    ]
}

token_data2_3 = {
    "contents": [
        {
            "parts": [
                {
                    "functionResponse": {
                        "name": "add",
                        "response": {
                            "name": "add",
                            "content": {
                                "text": "3 + 4 = 7"
                            }
                        }
                    }
                }
            ],
            "role": "function"
        }
    ]
}

token_data3 = {
    "contents": [
    ],
    "tools": [
        {
            "function_declarations": [
                {
                    "name": "add",
                    "description": "Add two numbers together.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "input1": {
                                "type": "number",
                            },
                            "input2": {
                                "type": "number",
                            }
                        },
                        "required": ["input1","input2"]
                    }
                }
            ]
        }
    ]
}

response = requests.post(token_url + "?key=" + api_key, json=token_data1, headers=headers)
print(response.text)

response = requests.post(token_url + "?key=" + api_key, json=token_data2_1, headers=headers)
print(response.text)

response = requests.post(token_url + "?key=" + api_key, json=token_data2_2, headers=headers)
print(response.text)

response = requests.post(token_url + "?key=" + api_key, json=token_data2_3, headers=headers)
print(response.text)

#response = requests.post(token_url + "?key=" + api_key, json=token_data3, headers=headers)
#print(response.text)



