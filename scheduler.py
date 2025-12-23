from ortools.sat.python import cp_model

def generate_schedule(people, tasks, time_slots, availability, max_hours, task_requirements):
    model = cp_model.CpModel()
    assign = {}

    for p in people:
        for t in tasks:
            for s in time_slots:
                assign[(p, t, s)] = model.NewBoolVar(f"{p}_{t}_{s}")

    for p in people:
        for s in time_slots:
            if not availability[p][s]:
                for t in tasks:
                    model.Add(assign[(p, t, s)] == 0)

    for p in people:
        for s in time_slots:
            model.Add(sum(assign[(p, t, s)] for t in tasks) <= 1)

    for t in tasks:
        for s in time_slots:
            model.Add(sum(assign[(p, t, s)] for p in people) == task_requirements[t])

    for p in people:
        model.Add(sum(assign[(p, t, s)] for t in tasks for s in time_slots) <= max_hours[p])

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return None

    return [(p, t, s) for (p, t, s), v in assign.items() if solver.Value(v) == 1]
