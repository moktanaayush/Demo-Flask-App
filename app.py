from flask import Flask, jsonify, request, abort

app = Flask(__name__)
items = [
    {"id": 1, "name": "Item One", "description": "First item"},
    {"id": 2, "name": "Item Two", "description": "Second item"}
]
next_id = 3


@app.route("/", methods=['GET'])  # Fixed E251: removed spaces around =
def home():
    return "Hey! Welcome to Chatbot Deployment! Happy Learning!"


@app.route('/items', methods=['GET'])  # Fixed E302: added 2 blank lines
def get_items():
    return jsonify(items)


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        abort(404)
    return jsonify(item)


@app.route('/items', methods=['POST'])
def create_item():
    global next_id
    data = request.get_json()
    if not data or 'name' not in data:  # Fixed E713: changed 'not ... in' to 'not in'
        abort(400)
    new_item = {
        "id": next_id,
        "name": data["name"],
        "description": data.get("description", "")
    }
    items.append(new_item)
    next_id += 1
    return jsonify(new_item), 201


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        abort(404)
    item["name"] = data.get("name", item["name"])
    item["description"] = data.get("description", item["description"])
    return jsonify(item)


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": True})


if __name__ == '__main__':
    app.run(debug=True)
