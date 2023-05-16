from flask import Blueprint, request, jsonify, render_template
from gpt import GetResponseGpt, CreateTitle, GetResponseGptWithContext
from models.get import GetConversationsInfo, GetConversation
from models.post import UpdateDialogue, CreateDialogue
ada_blueprint = Blueprint('/ada', __name__)

collection = "Ada"
base = "La siguientes preguntas seran sobre programcion, por favor encierra entre etiquetas <pre><code></code></pre> cuando escribas codigo de culquier lenjuaje.\n"
training = """
    Yo:¿Como se hace un bucle for en java?\n
    Tu: El bucle for en java se hace de la siguiente manera: \n <pre><code>for (int i = 0; i < 10; i++) { // código a ejecutar }</code></pre>\n
    Yo: ¿Como se hace el bucle "for" y el bucle "if" en python?\n
    Tu: El bucle for en python se hace de la siguente manera:
    <pre><code># Iteración a través de una lista\nfrutas = ["manzana", "plátano", "naranja"]\nfor fruta in frutas:\n    print(fruta)\n# Iteración a través de un rango de números\nfor i in range(1, 6):\n    print(i)</code></pre>\n
    Y el bucle if se declara de la siguente manera:\n
    <pre><code># Ejemplo básico\nedad = 18\nif edad >= 18:\n    print("Eres mayor de edad")</code></pre>
    Yo:
    """

@ada_blueprint.route('/ada', methods=['GET'])
def GetAdaDatas():
    try :
        id = request.args.get('id')
        conversations = GetConversationsInfo(collection)
        conversation = GetConversation(id,collection)
        return render_template('index.html', conversations=conversations, conversation=conversation,form_action="ada" ) 
    except Exception as e:
        return jsonify({'error': str(e)})
    
@ada_blueprint.route('/ada', methods=['POST'])
def GetAdaResponse():
    try :
        question = request.form.get('question')
        id = request.form.get('id')
        
        if id=="none":
            if question == "":
                conversations = GetConversationsInfo(collection)
                return render_template('index.html', conversations=conversations,form_action="ada" )
            full_question = base + training + "\nTu:"
            answer = GetResponseGpt(full_question)
            title = CreateTitle(question,answer)
            id = CreateDialogue(title,question,answer,collection,base,training)
            conversations = GetConversationsInfo(collection)
            conversation = GetConversation(id,collection)
            return render_template('index.html', conversations=conversations , conversation=conversation,form_action="ada" ) 
        else:
            conversation = GetConversation(id,collection)
            answer = GetResponseGptWithContext(question , conversation)
            UpdateDialogue(id,question,answer,collection)
            conversations = GetConversationsInfo(collection)
            conversation = GetConversation(id,collection)
            return render_template('index.html', conversations=conversations, conversation=conversation,form_action="ada" ) 
    except Exception as e:
        return jsonify({'error': str(e)})
    
    