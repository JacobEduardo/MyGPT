from flask import Blueprint, request, jsonify, render_template
from gpt import GetResponseGpt, CreateTitle, GetResponseGptWithContext, CreateResume
from models.get import GetConversationsInfo, GetConversation
from models.post import UpdateDialogue, CreateDialogue
conversation_blueprint = Blueprint('/conversation', __name__)

@conversation_blueprint.route('/conversation', methods=['GET'])
def GetResponse():
    try :
        id = request.args.get('id')
        collection = "Gpt"
        conversations = GetConversationsInfo(collection)
        conversation = GetConversation(id,collection)
        return render_template('index.html', conversations=conversations, conversation=conversation, form_action="conversation")   
    except Exception as e:
        return jsonify({'error': str(e)})
    
@conversation_blueprint.route('/conversation', methods=['POST'])
def PostResponse():
    try :
        question = request.form.get('question')
        id = request.form.get('id')
        collection = "Gpt"
        if id=="none":
            if question == "":
                conversations = GetConversationsInfo(collection)
                return render_template('index.html', conversations=conversations,form_action="conversation" ) 
            answer = GetResponseGpt(question)
            title = CreateTitle(question,answer)
            id = CreateDialogue(title, question, answer, collection)
            conversations = GetConversationsInfo(collection)
            conversation = GetConversation(id,collection)
            return render_template('index.html', conversations=conversations , conversation=conversation,form_action="conversation" ) 
        else:
            conversation = GetConversation(id,collection)
            resume = conversation["resume"]
            dialogue = conversation["dialogue"]
            last_questions_and_responses = "\nYo:" + dialogue[-1]["question"] + "\nTu:" +  dialogue[-1]["answer"] 
            resume = resume + last_questions_and_responses
            resume = CreateResume(resume)
            answer = GetResponseGptWithContext(question, resume)
            UpdateDialogue(id,question,answer,collection,resume)
            conversations = GetConversationsInfo(collection)
            conversation = GetConversation(id,collection)
            return render_template('index.html', conversations=conversations, conversation=conversation,form_action="conversation" ) 
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
