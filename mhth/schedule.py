from apscheduler.schedulers.blocking import BlockingScheduler
from sensors import update_data

scheduler = BlockingScheduler()

@scheduler.scheduled_job("interval", minutes=1)
def schedule_update_data():
    update_data()

scheduler.start()
