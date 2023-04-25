import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Say this is a test",
        max_tokens=7,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text

print(get_response("Say this is a test"))