from test_task_utility.config_reader import config


"""
This is a helper class to get the data from config and make it as a usable format
"""


class Helper:
    __host = config["host_config"]
    __port = config["host_port"]
    __path = config["host_path"]
    url = 'http://{host}:{port}/{path}'.format(host=__host, port=__port, path=__path)
    __logfile_name = config["logfile_name"]
    __logfile_path = config["logfile_path"]
    logfile = __logfile_path + __logfile_name














