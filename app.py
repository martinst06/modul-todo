from flask import Flask, render_template, request, redirect, url_for
from models import Task

app = Flask(__name__)

tasks = []
done_tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/done-tasks')
def done():
    return render_template('done.html', done_tasks=done_tasks)

@app.route('/create_task', methods=['POST'])
def create_task():
    task_name = request.form.get('task_name')
    task = Task(name=task_name)
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete_task_index/<string:task_id>')
def delete_task_index(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return redirect(url_for('index'))

@app.route('/delete_task_done/<string:task_id>')
def delete_task_done(task_id):
    global done_tasks
    done_tasks = [task for task in done_tasks if task.id != task_id]
    return redirect(url_for('done'))

@app.route('/mark_done/<string:task_id>')
def mark_done(task_id):
    global tasks, done_tasks
    for task in tasks:
        if task.id == task_id:
            done_tasks.append(task)
            tasks.remove(task)
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
