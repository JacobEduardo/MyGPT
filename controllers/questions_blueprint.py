from flask import Blueprint, request, jsonify
from gpt import get_response

questions_blueprint = Blueprint('questions', __name__)

@questions_blueprint.route('/questions', methods=['GET'])
def say_question():
    #data = request.json
    #question = data.get('question', None)
    #return jsonify({"error": "user_id no proporcionado"}), 400
    return get_response("Say this is a test")

