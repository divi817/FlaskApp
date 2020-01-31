from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    done =  db.Column(db.Boolean)


@app.route('/')
def home():
    taskz = Task.query.all()
    return render_template("index.html", tasks = taskz)


@app.route('/create-task', methods=['POST'])
def create():
    new_task = Task(content=request.form['content'], done=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<id>')
def delete(id):
    task = Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))

if __name__== '__main__':
    app.run(debug=True)
