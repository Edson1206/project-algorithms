def study_schedule(permanence_period, target_time):
    students = 0
    try:
        for entry, exit in permanence_period:
            if entry <= target_time <= exit:
                students += 1
        return students
    except TypeError:
        return None
