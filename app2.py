from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
users = []

# GET: List all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST: Add a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User added!", "user": data}), 201

# PUT: Update an existing user by name
@app.route('/users/<string:name>', methods=['PUT'])
def update_user(name):
    data = request.get_json()
    for user in users:
        if user['name'] == name:
            user.update(data)
            return jsonify({"message": "User updated!", "user": user})
    return jsonify({"error": "User not found"}), 404

# DELETE: Remove user by name
@app.route('/users/<string:name>', methods=['DELETE'])
def delete_user(name):
    global users
    users = [user for user in users if user['name'] != name]
    return jsonify({"message": f"User '{name}' deleted if existed."})

if __name__ == '__main__':
    app.run(debug=True)
