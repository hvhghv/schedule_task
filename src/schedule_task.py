import schedule
import json
import logging
import io
import multiprocessing
import time
import subprocess
import threading
import datetime
import os

def process_task(name,command,path):

    os_run = subprocess.Popen(
        command,
        shell=True,
        bufsize=-1,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=path
    )

    file = io.TextIOWrapper(os_run.stdout)

    return name,file.read()


if __name__ == '__main__':


    pool = multiprocessing.Pool(processes=2)


    dir_path = os.path.dirname(os.path.abspath(__file__))

    logging.basicConfig(
        filename=os.path.join(dir_path,'logging','logging.txt'),
        filemode='w',
        level=logging.INFO,
        format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(funcName)s\n%(message)s ',

    )

    logging_get = logging.getLogger()


    with open(os.path.join(dir_path,'task','task.json'), encoding="utf-8") as f:
        task: dict = json.load(f)


    def process_callback(result):
        logging_get.info("%s %s" % (result[0], result[1]))
        logging_get.info('%s End' % result[0])


    def process_error_callback(result):
        logging_get.error(result)


    def late_task(sec_all,name,commend,path):
        time.sleep(sec_all)
        pool.apply_async(process_task, args=(name, commend, path), callback=process_callback,
                         error_callback=process_error_callback)

    def start_commend(name,commend,path):
        logging_get.info('%s Start' % name)
        pool.apply_async(process_task,args=(name,commend,path),callback=process_callback,error_callback=process_error_callback)

    def check0_task(sec_all:int,name,commend,path):
        schedule.every(sec_all).seconds.do(start_commend,name,commend,path)

    def check1_task(hour:int,min:int,sec:int,name,commend,path):
        now_time = datetime.time(hour=hour,minute=min,second=sec)
        schedule.every().day.at(now_time.strftime("%H:%M:%S")).do(start_commend,name,commend,path)

    def check2_task(sec_all,name,commend,path):
        threading.Thread(target=late_task,args=(sec_all,name,commend,path,),daemon=True).start()

    for k in task.keys():
        if task[k]["check"] == 0:
            check0_task(task[k]["hour"]*3600 + task[k]["min"]*60 + task[k]["sec"],task[k]["name"],task[k]["command"],task[k]["path"])

        elif task[k]["check"] == 1:
            check1_task(task[k]["hour"],task[k]["min"],task[k]["sec"],task[k]["name"],task[k]["command"],task[k]["path"])

        elif task[k]["check"] == 2:
            check2_task(task[k]["hour"] * 3600 + task[k]["min"] * 60 + task[k]["sec"], task[k]["name"],
                        task[k]["command"], task[k]["path"])

    while True:
        schedule.run_pending()
        time.sleep(1)
