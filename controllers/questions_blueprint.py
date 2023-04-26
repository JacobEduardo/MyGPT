from flask import Blueprint, request, jsonify, render_template
from gpt import get_response
from models.post import Post


questions_blueprint = Blueprint('questions', __name__)

@questions_blueprint.route('/questions', methods=['POST'])
def GetResponse():
    question = request.form['question']
    result = get_response(question)

    return render_template('index.html', result=result)