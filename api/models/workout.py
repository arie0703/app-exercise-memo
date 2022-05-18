from api.database import db, ma

class Workout(db.Model):
  __tablename__ = 'workouts'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(50), nullable=False)

  def __repr__(self):
    return '<Workout %r>' % self.name

  def getWorkoutList():

    workout_list = db.session.query(Workout).all()

    if workout_list == None:
      return []
    else:
      return workout_list

  def registWorkout(workout):
    record = Workout(
      name = workout['name'],

    )

    db.session.add(record)
    db.session.commit()

    return workout

class WorkoutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        fields = ('id', 'name')