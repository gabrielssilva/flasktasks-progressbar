from flask import render_template
from flasktasks.models import Status


def mission_list_item_additional_content(mission):
    all_tasks = mission.tasks
    if all_tasks.count() > 0:
        completed_tasks = mission.tasks.filter_by(status=Status.DONE.value)
        progress = (completed_tasks.count() / all_tasks.count()) * 100
    else:
        progress = 0

    return render_template('flasktasks_progressbar/progress_bar.html',
                           progress=progress)
