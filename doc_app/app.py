
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import routes after initializing the app and db
from routes import *  # Import routes from routes.py

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
