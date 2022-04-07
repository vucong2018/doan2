from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/test_connect', methods=['GET'])
def test_connect():
    response = jsonify({'data':'Connect success!!!'})
    response.status_code = 200
    return response

if __name__ == '__main__':
    app.run()

