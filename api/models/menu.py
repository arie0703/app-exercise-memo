from database import db, ma
from sqlalchemy import ForeignKey
from .workout import Workout

class Menu(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reps = db.Column(db.Integer, nullable=False, default=0)
    set_count = db.Column(db.Integer, nullable=False, default=0)
    weight = db.Column(db.Integer, nullable=False, default=0)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id", ondelete='CASCADE'), nullable=False)
    template_id = db.Column(db.Integer, db.ForeignKey("templates.id", ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return '<Menu %r>' % self.name

    def getMenu():

        menu_list = db.session.query(Menu).all()

        if menu_list == None:
            return []
        else:
            return menu_list


    def getSetMenu(template_id):
        menus = db.session.query(Workout.name, Menu.weight, Menu.reps, Menu.set_count).join(Workout, Menu.workout_id == Workout.id).filter(Menu.template_id == template_id).all()
        return menus

    def createMenu(menu):
        record = Menu(
            reps = menu['reps'],
            set_count = menu['set_count'],
            weight = menu['weight'],
            workout_id = menu['workout_id'],
            template_id = menu['template_id'],
        )

        db.session.add(record)
        db.session.commit()

        return menu

class MenuSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Menu
        fields = ('id', 'reps', 'set_count', 'weight', 'workout_id', 'template_id', 'name')


