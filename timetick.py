from datetime import datetime
import time
import os
from apscheduler.schedulers.blocking import BlockingScheduler

def sendmsg(text):
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(sendmsg, 'date', run_date=datetime(2019, 7, 19, 21, 42, 0), args=['text'])
    scheduler.start()