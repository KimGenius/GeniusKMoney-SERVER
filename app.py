from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/test')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
