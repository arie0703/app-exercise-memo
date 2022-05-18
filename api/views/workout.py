from flask import Blueprint, request, make_response, jsonify
from models import Workout, WorkoutSchema
import json

# ルーティング設定
workout_router = Blueprint('workout_router', __name__)

@workout_router.route('/workouts', methods=['GET'])
def getWorkoutList():

  workouts = Workout.getWorkoutList()
  workout_schema = WorkoutSchema(many=True)

  return make_response(jsonify({
    'code': 200,
    'workouts': workout_schema.dump(workouts)
  }))

@workout_router.route('/workouts', methods=['POST'])
def registWorkout():

  # jsonデータを取得する
  jsonData = json.dumps(request.json)
  workoutData = json.loads(jsonData)

  workout = Workout.registWorkout(workoutData)
  workout_schema = WorkoutSchema(many=True)

  return make_response(jsonify({
    'code': 200,
    'workout': workout
  }))