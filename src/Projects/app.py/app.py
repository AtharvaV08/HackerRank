from flask import Flask, render_template, request, redirect, url_for
import pyttsx3
from datetime import datetime
import threading
import time

app = Flask(__name__)

# In-memory storage for tasks
tasks = []
completed_tasks = []

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def check_due_tasks():
    while True:
        current_time = datetime.now().strftime("%H:%M")
        for task in tasks:
            if not task['completed'] and task['due_time'] == current_time:
                speak(f"Task due: {task['content']}. Please complete it.")
        time.sleep(60)  # Check every minute

# Start background thread to monitor task due times
threading.Thread(target=check_due_tasks, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, completed_tasks=completed_tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form['task']
    due_time = request.form['due_time']
    if task_content and due_time:
        task = {'id': len(tasks) + 1, 'content': task_content, 'due_time': due_time, 'completed': False}
        tasks.append(task)
        speak(f"New task added: {task_content}, due at {due_time}")
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    new_content = request.form['task']
    new_due_time = request.form['due_time']
    for task in tasks:
        if task['id'] == task_id:
            task['content'] = new_content
            task['due_time'] = new_due_time
            speak(f"Task updated: {new_content}, new due time: {new_due_time}")
            break
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            completed_tasks.append(task)
            tasks.remove(task)
            speak(f"Task completed: {task['content']}")
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks, completed_tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    completed_tasks = [task for task in completed_tasks if task['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)