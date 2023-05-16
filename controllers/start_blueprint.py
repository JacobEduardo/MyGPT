from flask import Blueprint, request, render_template
from models.get import GetConversationsInfo
start_blueprint = Blueprint('/', __name__)

@start_blueprint.route('/', methods=['GET'])
def index():
    conversations = GetConversationsInfo()
    return render_template('index.html', conversations=conversations)   