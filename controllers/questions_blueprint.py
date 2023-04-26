from flask import Blueprint, request, jsonify, render_template
from gpt import get_response


questions_blueprint = Blueprint('questions', __name__)

@questions_blueprint.route('/questions', methods=['GET'])
def GetResponse():
    try :
        question = request.args.get('question')
        result = get_response(question)
        return render_template('result.html', result=result)
    except Exception as e:
        return jsonify({'error': str(e)})