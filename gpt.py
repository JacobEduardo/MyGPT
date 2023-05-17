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
    prompt = ("Crea un titulo corto que resuma esta pregunta y respuesta , la pregunta es: '"+question+".\n y la respuesta es: "+answer+" .\n\nTitulo:"),
    return GetResponseGpt(prompt)


def GetResponseGptWithContext(question, conversation, collection):
    question = question
    collection = collection
    dialogue = conversation["dialogue"]
    base = conversation["base"]

    for i in dialogue:
        conversation_to_text += "Yo:" + i["question\n"] + "Tu:" + i["answer\n"]
    
    resume = GetResume(conversation_to_text)
    full_question = base + resume 
    response = GetResponseGpt(full_question)
    return response 

def GetResume(full_question):
    if len(full_question) > 2000:
        promt = "resume la siguente conversacion a menos de 1000 caracteres manteniendo la estructura:\n" + full_question + "\n\n"
        resume = GetResponseGpt(promt)
        return resume
    else:
        return full_question