import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def GetResponseGpt(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text

def CreateTitle(question, answer):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=("Crea un titulo corto que resuma esta pregunta y respuesta , la pregunta es: '"+question+".\n y la respuesta es: "+answer+" .\n\nTitulo:"),
        max_tokens=1000,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text

def GetAgataResponse(prompt):
    response = openai.Completion.create(
        pre_promt=
        "Agata: Donde esta la capital de francia?",
        model="davinci",
        prompt=prompt,
        max_tokens=1000,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text