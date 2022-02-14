from datetime import datetime, timedelta

from src.config import api, DAY
from src.utils import count_secodns, fetch_segment


def set_priorities(label: str, blue: str, yellow: str, red: str):
    blue_time = count_secodns(fetch_segment(blue))
    yellow_time = count_secodns(fetch_segment(yellow))
    red_time = count_secodns(fetch_segment(red))
    tasks = api.get_tasks(filter=f"@{label}")
    for item in tasks:
        task = item.__dict__
        due = task['due'].__dict__['datetime']
        # for heroku + 3 hours
        dt_now = datetime.now() + timedelta(hours=3)
        if due:
            dt = datetime.strptime(due, '%Y-%m-%dT%H:%M:%SZ')
            delta_seconds = (dt + timedelta(hours=3) - dt_now).seconds
        else:
            date_no_time = task['due'].__dict__['date']
            dt = datetime.strptime(date_no_time, '%Y-%m-%d')
            delta_seconds = ((dt + timedelta(hours=3) - dt_now).days) * DAY
        if delta_seconds < red_time or (dt + timedelta(hours=3) - dt_now).days < 0:
            api.update_task(task['id'], priority=4)
        elif delta_seconds < yellow_time:
            api.update_task(task['id'], priority=3)
        elif delta_seconds < blue_time:
            api.update_task(task['id'], priority=2)
        else:
            api.update_task(task['id'], priority=1)
