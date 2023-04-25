from flask import Flask

from controllers.questions_blueprint import questions_blueprint

app = Flask(__name__)

app.register_blueprint(questions_blueprint)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)