from flask import Flask, render_template, request
from scheduler import generate_schedule
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        people = [p.strip() for p in request.form.get("people").split(",")]
        tasks = [t.strip() for t in request.form.get("tasks").split(",")]
        time_slots = [s.strip() for s in request.form.get("slots").split(",")]

        availability = {p: {s: True for s in time_slots} for p in people}
        max_hours = {p: len(time_slots) for p in people}
        task_requirements = {t: 1 for t in tasks}

        schedule = generate_schedule(
            people, tasks, time_slots,
            availability, max_hours, task_requirements
        )

        return render_template("result.html", schedule=schedule)

    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
