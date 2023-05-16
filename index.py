from flask import Flask

from controllers.conversation_blueprint import conversation_blueprint
from controllers.start_blueprint import start_blueprint
from controllers.ada_blueprint import ada_blueprint

app = Flask(__name__)

app.register_blueprint(conversation_blueprint)
app.register_blueprint(start_blueprint)
app.register_blueprint(ada_blueprint)

if __name__ == '__main__':
    app.run(debug=True)