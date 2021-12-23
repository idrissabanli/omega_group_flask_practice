from sqlalchemy.sql import func

from extentions import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    message = db.Column(db.Text, nullable=False)

    __table_args__ = {'extend_existing': True} 

    def __repr__(self):
        return f'<User {self.name}>'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)

    blogs = db.relationship('Blog', backref=db.backref('category', lazy=True))

    def __repr__(self):
        return f'<User {self.title}>'


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    title = db.Column(db.String(100), nullable=False)
    brief = db.Column(db.String(100))
    author = db.Column(db.String(40), nullable=False)
    content = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return self.title
