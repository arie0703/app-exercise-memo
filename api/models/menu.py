from database import db, ma
from sqlalchemy import ForeignKey

class Menu(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reps = db.Column(db.Integer, nullable=False, default=0)
    set_count = db.Column(db.Integer, nullable=False, default=0)
    weight = db.Column(db.Integer, nullable=False, default=0)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id", ondelete='CASCADE'), nullable=False)
    template_id = db.Column(db.Integer, db.ForeignKey("templates.id", ondelete='CASCADE'), nullable=False)


