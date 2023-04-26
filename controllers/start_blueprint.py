from flask import Blueprint, request, render_template
from gpt import get_response

start_blueprint = Blueprint('/', __name__)

@start_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html', resultado="resultardo")
