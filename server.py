from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

check_list = []

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return jsonify(check_list)
    if request.method == 'POST':
        request_data = request.get_json()
        check_list.append(request_data)
        return jsonify(check_list)

if __name__ == '__main__':
    app.run(debug=True)