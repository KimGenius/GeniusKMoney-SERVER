from flask import Flask
from flask_cors import CORS
from flask import jsonify
from flask import request
import Database

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

db = lambda: Database.GeniusKMoney()


@app.route('/api/customers', methods=['GET', 'POST'])
def customers():
    if request.method == 'GET':
        res = db().list_customers()
        return jsonify(res)
    elif request.method == 'POST':
        return 'Create Customer!\n'


@app.route('/api/histories', methods=['GET', 'POST'])
def histories():
    if request.method == 'GET':
        res = db().list_money_histories()
        return jsonify(res)
    elif request.method == 'POST':
        return 'Create History!\n'


if __name__ == '__main__':
    app.run()
