"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:myPassword@localhost:5432/cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/cupcakes')
def get_cupcakes():
    cupcakes = Cupcake.query.all()
    cupcakes_serialized = [c.serialized for c in cupcakes]
    return jsonify(cupcakes=cupcakes_serialized)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialized)

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Create cupcake from form data & return it.

    Returns JSON {'cupcake': {id, flavor, size, rating, image}}
    """

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    # Return w/status code 201 --- return tuple (json, status)
    return ( jsonify(cupcake=new_cupcake.serialized), 201 )

@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def update_cupcake(id):
    """Update cupcake from form data & return it.

    Returns JSON {'cupcake': {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialized)


@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    """Delete cupcake.
    Returns message if was deleted successfully.
    """
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="deleted")