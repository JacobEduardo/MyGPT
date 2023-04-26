from flask import Blueprint, request, jsonify, render_template
from gpt import get_response

questions_blueprint = Blueprint('questions', __name__)

@questions_blueprint.route('/questions', methods=['GET'])
def say_question():
    #return jsonify({"error": "user_id no proporcionado"}), 400
    resultardo = get_response("Say this is a test")
    return render_template('result.html', resultado=resultardo)
