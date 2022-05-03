from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return ('hello world')

@app.route('/<string:name>')
def name(name):
    return (name)

if __name__ == '__main__':
    app.run(debug=True)