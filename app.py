from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task list (no database)
tasks = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/tasks", methods=["GET", "POST"])
def manage_tasks():
    if request.method == "POST":
        # Get form data
        task_name = request.form.get("task_name")
        description = request.form.get("description")
        status = request.form.get("status", "Pending")  # Default status is "Pending"
        
        # Add the task to the list
        tasks.append({
            "name": task_name,
            "description": description,
            "status": status
        })
        return redirect(url_for("task_dashboard"))
    
    return render_template("add_task.html")

@app.route('/tasks/dashboard')
def task_dashboard():
    return render_template("task_dashboards.html", tasks=tasks)

@app.route("/tasks/delete/<int:task_id>")
def delete_task(task_id):
    # Delete task by ID if it exists in the list
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("manage_tasks"))

if __name__ == "__main__":
    app.run(debug=True)
