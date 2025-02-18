from app import app, db
from models import User
from flask import jsonify, render_template


@app.route('/')
def index():
    return render_template('sample.html')


@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])
