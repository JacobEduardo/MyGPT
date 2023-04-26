from flask import Blueprint, request, render_template

start_blueprint = Blueprint('/', __name__)

@start_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html', resultado="resultardo")