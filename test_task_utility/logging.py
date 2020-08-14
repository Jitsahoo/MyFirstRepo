import logging


from test_task_utility.utility_helper import Helper


"""
This is used to initialize the log object for logging purpose
"""


def initialize_log():

    logging.basicConfig(filename=Helper.logfile, format='%(asctime)s %(message)s', filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    return logger

logger = initialize_log();


