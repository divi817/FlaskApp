from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/')

def home():
    return 'Hello World'

if __name__== '__main__':
    app.run(debug=True)
