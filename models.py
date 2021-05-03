"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """Cupcake."""

    __tablename__ = "cupcakes"

# id: a unique primary key that is an auto-incrementing integer
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)
# flavor: a not-nullable text column
    flavor = db.Column(
        db.Text,
        nullable=False
    )
# size: a not-nullable text column
    size = db.Column(
        db.Text,
        nullable=False
    )
# rating: a not-nullable column that is a float
    rating = db.Column(
        db.Float,
        nullable=False
    )
# image: a non-nullable text column. If an image is not given, default to https://tinyurl.com/demo-cupcake
    image = db.Column(
        db.Text,
        nullable=False,
        default='https://tinyurl.com/demo-cupcake'
    )

    @property
    def serialized(self):
        """Serialize a Cupcake SQLAlchemy obj to dictionary."""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image,
        }