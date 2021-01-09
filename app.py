"""Main app"""


import os
from flask import Flask, request, jsonify
from marshmallow import ValidationError
from model import db, Parent, Child
from schemas import parent_schema, parents_schema, child_schema, children_schema


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/parent", methods=["POST"])
def create_parent():
    """Create a parent"""
    # Handle input data
    try:
        json_data = request.get_json()
    except:
        return {"error": "Invalid input data"}, 400
    if not json_data:
        return {"error": "No input data provided"}, 400
    # Validate input data
    try:
        data = parent_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 422
    # Load data
    first_name = data["first_name"]
    last_name = data["last_name"]
    street = data["street"]
    city = data["city"]
    state = data["state"]
    zip_code = data["zip_code"]

    parent = Parent(first_name, last_name, street, city, state, zip_code)
    db.session.add(parent)
    db.session.commit()
    return parent_schema.dump(parent), 201


@app.route("/parent", methods=["GET"])
def show_parent():
    """Show all parent"""
    parents = Parent.query.all()
    if not parents:
        return {"msg": "Parent not found"}, 404
    result = parents_schema.dump(parents)
    return jsonify(result), 200


@app.route("/parent/<int:parent_id>", methods=["PUT"])
def update_parent(parent_id):
    """Update a parent"""
    # Check parent
    parent = Parent.query.get(parent_id)
    if not parent:
        return {"msg": "Parent not found"}, 404
    # Handle input data
    try:
        json_data = request.get_json()
    except:
        return {"error": "Invalid input data"}, 400
    if not json_data:
        return {"error": "No input data provided"}, 400
    # Validate input data
    try:
        data = parent_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 422
    # Load data
    parent.first_name = data["first_name"]
    parent.last_name = data["last_name"]
    parent.street = data["street"]
    parent.city = data["city"]
    parent.state = data["state"]
    parent.zip_code = data["zip_code"]

    db.session.commit()
    return parent_schema.dump(parent), 201


@app.route("/parent/<int:parent_id>", methods=["DELETE"])
def delete_parent(parent_id):
    """Delete a parent"""
    parent = Parent.query.get(parent_id)
    if not parent:
        return {"error": "Parent not found"}, 404
    db.session.delete(parent)
    db.session.commit()
    return parent_schema.dump(parent), 202


@app.route("/parent/<int:parent_id>/child", methods=["POST"])
def create_child(parent_id):
    """Create a child"""
    # Check parent
    parent = Parent.query.get(parent_id)
    if not parent:
        return {"error": "Parent not found"}, 404
    # Handle input data
    try:
        json_data = request.get_json()
    except:
        return {"error": "Invalid input data"}, 400
    if not json_data:
        return {"error": "No input data provided"}, 400
    # Validate input data
    try:
        data = child_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 422

    first_name = data["first_name"]
    last_name = data["last_name"]
    child = Child(first_name, last_name, parent_id)
    db.session.add(child)
    db.session.commit()
    return child_schema.dump(child), 201


@app.route("/parent/<int:parent_id>/child", methods=["GET"])
def show_child(parent_id):
    """Show all child"""
    parent = Parent.query.get(parent_id)
    if not parent:
        return {"msg": "Parent not found"}, 404
    children = parent.child_relation
    if not children:
        return {"msg": "Child not found"}, 404
    result = children_schema.dump(children)
    return jsonify(result), 200


@app.route("/parent/<int:parent_id>/child/<int:child_id>", methods=["PUT"])
def update_child(parent_id, child_id):
    """Update a child"""
    # Check parent and related child
    parent = Parent.query.get(parent_id)
    if not parent:
        return {"msg": "Parent not found"}, 404
    children = parent.child_relation
    if not children:
        return {"msg": "Child not found"}, 404

    # Input check
    try:
        json_data = request.get_json()
    except:
        return {"error": "Invalid input data"}, 400
    if not json_data:
        return {"error": "No input data provided"}, 400

    # Validate and load data for correct child
    for child in children:
        if child.id == child_id:
            try:
                data = child_schema.load(json_data)
            except ValidationError as err:
                return err.messages, 422
            child.first_name = data["first_name"]
            child.last_name = data["last_name"]
            db.session.commit()
            return child_schema.dump(data), 202
    return {"error": "Child not found"}, 404


@app.route("/parent/<int:parent_id>/child/<int:child_id>", methods=["DELETE"])
def delete_child(parent_id, child_id):
    """Delete a child"""
    # Check parent and child
    parent = Parent.query.get(parent_id)
    if not parent:
        return {"msg": "Parent not found"}, 404
    children = parent.child_relation
    if not children:
        return {"msg": "Child not found"}, 404

    for child in children:
        if child.id == child_id:
            db.session.delete(child)
            db.session.commit()
            return parent_schema.dump(child), 202
    return {"error": "Child not found"}, 404


@app.errorhandler(404)
def resource_not_found(err):
    """404 handle"""
    return jsonify(error=str(err)), 404


@app.errorhandler(405)
def method_not_allowed(err):
    """405 handle"""
    return jsonify(error=str(err)), 405


if __name__ == "__main__":
    db.create_all()
    app.run()
