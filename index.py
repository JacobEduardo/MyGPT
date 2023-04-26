from flask import Flask

from controllers.questions_blueprint import questions_blueprint
from controllers.start_blueprint import start_blueprint

app = Flask(__name__)

app.register_blueprint(questions_blueprint)
app.register_blueprint(start_blueprint)

if __name__ == '__main__':
    app.run(debug=True)