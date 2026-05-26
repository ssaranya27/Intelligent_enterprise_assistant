import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_ai_response(user_message):

    prompt = f"""

    You are an Enterprise AI IT Support Assistant.

    Rules:
    - Give professional answers
    - Keep answers short
    - Maximum 3 lines
    - Give troubleshooting steps
    - Avoid unnecessary explanations

    User Question:
    {user_message}

    """

    payload = {

        "model": "mistral",

        "prompt": prompt,

        "stream": False,

        "options": {
            "num_predict": 120
        }

    }

    response = requests.post(OLLAMA_URL, json=payload)

    data = response.json()

    return data["response"]