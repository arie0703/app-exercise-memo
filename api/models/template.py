from database import db, ma
from .menu import Menu

class Template(db.Model):
    __tablename__ = 'templates'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)