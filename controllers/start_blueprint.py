from flask import Blueprint, request, render_template
from models.get import GetConversations
start_blueprint = Blueprint('/', __name__)

@start_blueprint.route('/', methods=['GET'])
def index():
    conversations = GetConversations()
    return render_template('index.html', conversations=conversations)   