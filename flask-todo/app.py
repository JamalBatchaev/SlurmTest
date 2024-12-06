from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:12345@localhost/postgres'
db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'flask_tasks'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    is_done = db.Column(db.Boolean, nullable=False, default=False)
    start_time= db.Column(db.DateTime, nullable=True, default=None)
    end_time= db.Column(db.DateTime, nullable=True, default=None)
    is_descr= db.Column(db.Boolean, nullable=False, default=False)


@app.route('/')
def index():
    return render_template('base.html', tasks=Task.query.order_by(Task.id).all())

@app.route('/add', methods=["POST"])
def add():
    text = request.form.get('task')
    description = request.form.get('description')
    db.session.add(
        Task(text=text, description=description, start_time=datetime.now().replace(microsecond=0))
    )
    print (text)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/clear', methods=["POST"])
def clear():
    Task.query.delete()    
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/done/<int:task_id>')
def done(task_id):
    task = Task.query.get(task_id)   
    task.is_done = True 
    task.end_time=datetime.now().replace(microsecond=0)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)   
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

#переоткрывает задачу
@app.route('/reopen/<int:task_id>')
def reopen(task_id):
    task = Task.query.get(task_id)   
    task.is_done = False 
    task.start_time=datetime.now().replace(microsecond=0)
    task.end_time=None
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('index'))

#показывает/скрывает сведения о задаче
@app.route('/is_descr_show/<int:task_id>')
def is_descr_show(task_id):
    task = Task.query.get(task_id)   
    if task.is_descr==False:
        task.is_descr=True
    else:
        task.is_descr=False
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
    
