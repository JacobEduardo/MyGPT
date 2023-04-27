from flask import Blueprint, request, jsonify, render_template
from gpt import GetResponseGpt, CreateTitle
from models.get import GetConversations, GetConversation
from models.post import UpdateDialogue, CreateDialogue
conversation_blueprint = Blueprint('/conversation', __name__)

@conversation_blueprint.route('/conversation', methods=['GET'])
def GetResponse():
    try :
        id = request.args.get('id')
        conversations = GetConversations()
        conversation = GetConversation(id)
        return render_template('index.html', conversations=conversations, conversation=conversation)   
    except Exception as e:
        return jsonify({'error': str(e)})
    
@conversation_blueprint.route('/conversation', methods=['POST'])
def PostResponse():
    try :
        question = request.form.get('question')
        id = request.form.get('id')
        if id=="none":
            if question == "":
                conversations = GetConversations()
                return render_template('index.html', conversations=conversations) 
            answer = GetResponseGpt(question)
            title = CreateTitle(question,answer)
            id = CreateDialogue(title,question,answer)
            conversations = GetConversations()
            conversation = GetConversation(id)
            return render_template('index.html', conversations=conversations , conversation=conversation) 
        else:
            answer = GetResponseGpt(question)
            UpdateDialogue(id,question,answer)
            conversation = GetConversation(id)
            conversations = GetConversations()
            return render_template('index.html', conversations=conversations, conversation=conversation) 
    except Exception as e:
        return jsonify({'error': str(e)})
    
