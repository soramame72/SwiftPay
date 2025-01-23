from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}
transactions = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    if username in users:
        return jsonify({'message': 'User already exists'}), 400
    users[username] = {'balance': 0}
    return jsonify({'message': 'User registered successfully'}), 200

@app.route('/balance/<username>', methods=['GET'])
def balance(username):
    user = users.get(username)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'balance': user['balance']}), 200

@app.route('/transaction', methods=['POST'])
def transaction():
    data = request.json
    sender = data['sender']
    receiver = data['receiver']
    amount = data['amount']

    if sender not in users or receiver not in users:
        return jsonify({'message': 'User not found'}), 404
    if users[sender]['balance'] < amount:
        return jsonify({'message': 'Insufficient balance'}), 400

    users[sender]['balance'] -= amount
    users[receiver]['balance'] += amount
    transactions.append({
        'sender': sender,
        'receiver': receiver,
        'amount': amount
    })
    return jsonify({'message': 'Transaction successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

users = {}
transactions = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    if username in users:
        return jsonify({'message': 'User already exists'}), 400
    users[username] = {'balance': 0}
    return jsonify({'message': 'User registered successfully'}), 200

@app.route('/balance/<username>', methods=['GET'])
def balance(username):
    user = users.get(username)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'balance': user['balance']}), 200

@app.route('/transaction', methods=['POST'])
def transaction():
    data = request.json
    sender = data['sender']
    receiver = data['receiver']
    amount = data['amount']

    if sender not in users or receiver not in users:
        return jsonify({'message': 'User not found'}), 404
    if users[sender]['balance'] < amount:
        return jsonify({'message': 'Insufficient balance'}), 400

    users[sender]['balance'] -= amount
    users[receiver]['balance'] += amount
    transactions.append({
        'sender': sender,
        'receiver': receiver,
        'amount': amount
    })
    return jsonify({'message': 'Transaction successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)
