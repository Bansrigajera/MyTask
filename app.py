from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])  # This only allows GET requests
def hello():
    name = request.args.get('name', 'Guest')
    return jsonify({'message': f'Hello, {name}!'})

@app.route('/add', methods=['POST'])  # This only allows POST requests
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
