from flask import Blueprint, request, jsonify, render_template
from gpt import GetResponseGpt, CreateTitle
from models.get import GetAdaConversations, GetAdaConversation
from models.post import UpdateDialogue, CreateDialogue
ada_blueprint = Blueprint('/ada', __name__)

@ada_blueprint.route('/ada', methods=['GET'])
def GetAdaDatas():
    try :
        id = request.args.get('id')
        conversations = GetAdaConversations()
        conversation = GetAdaConversation(id)
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
                conversations = GetAdaConversations()
                return render_template('index.html', conversations=conversations,form_action="ada" ) 
            resume = """
            La siguientes preguntas seran sobre programcion, por favor encierra entre etiquetas <code></code> cuando escribas codigo de culquier lenjuaje.\n
            Yo:¿Como se hace un bucle for en java?\n
            Tu: El bucle for en java se hace de la siguiente manera: \n <code>for (int i = 0; i < 10; i++) { // código a ejecutar }</code>\n
            Yo:
            """
            full_question = resume + question + "\nTu:"
            answer = GetResponseGpt(full_question)
            print("respuesta::", answer)
            title = CreateTitle(question,answer)
            collection_name = "Ada"
            id = CreateDialogue(title,question,answer,collection_name,resume)
            conversations = GetAdaConversations()
            conversation = GetAdaConversation(id)
            return render_template('index.html', conversations=conversations , conversation=conversation,form_action="ada" ) 
        else:
            answer = GetResponseGpt(question)
            collection_name = "Ada"
            UpdateDialogue(id,question,answer,collection_name)
            conversations = GetAdaConversations()
            conversation = GetAdaConversation(id)
            return render_template('index.html', conversations=conversations, conversation=conversation,form_action="ada" ) 
    except Exception as e:
        return jsonify({'error': str(e)})
    
    