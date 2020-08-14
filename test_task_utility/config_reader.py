import json
import os

path = os.getcwd() + "/../resources/"
configfile = path+"config.json"
task = path+"task.json"



def _load_config(configfile=configfile):
    with open(configfile) as conf:
        config = json.load(conf)
    return config


config = _load_config()


def _load_create_task_payload(create_task = task):
    with open(create_task) as task:
        create_task = json.load(task)
    return create_task["create_task"]


create_task = _load_create_task_payload()


def _load_update_task_payload(update_task = task):
    with open(update_task) as task:
        update_task = json.load(task)
    return update_task["update_task"]


update_task = _load_update_task_payload()




