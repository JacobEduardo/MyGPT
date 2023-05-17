import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def GetResponseGpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

def CreateTitle(question, answer):
    prompt = ("Crea un titulo corto que resuma esta pregunta y respuesta , la pregunta es: '"+question+".\n y la respuesta es: "+answer+" .\n\nTitulo:"),
    prompt = str(prompt)
    return GetResponseGpt(prompt)


def GetResponseGptWithContext(question, resume, base=""):
    prompt = resume + "\n" + base + "\nYo:" +  question + "\nTu:"
    response = GetResponseGpt(prompt)
    return response 

def CreateResume(prompt):
    caracter = len(prompt)
    if caracter > 1000:
        prompt = "resume la siguente conversacion en menos de 500 caracteres:\n" + prompt 
        prompt = GetResponseGpt(prompt)
        prompt = "Estas manteniendo una conversacion: " + prompt
        return prompt
    else:
        return prompt