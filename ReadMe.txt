Instructions : task_server_automation
=====================================

Prerequisites:
-------------
Python 3.x installed
todolist_mock_server should run in you local
path to get https://githttps://github.com/aquaomri/todolist_mock_server

Installations
-------------
Install the packages from setup.py using below command

    python setup.py install

Configuration
-------------
 Configuration values in resources\config.json: for the todolist_mock_server
   -> host_config :- where the todolist_mock_server is running
   -> host_port :- in Which port the todolist_mock_server is running
   ->host_path :- path to access the endpoint
   -> logfile_name :- name of the logfile where the log should be written
   ->logfile_path :- path of the directory where the logfile should be created
 Configure values for create task  and update task in resources\task.json


Tests Execution
---------------
Navigate to task_server_automation\test_endpoint in commandline and execute below command
 pytest --alluredir=..\test_report\myreport

After execution run below command to generate the allure report
 allure generat --clean ..\test_report\myreport

To get the overview report pytest --html=../test_report/report.html

Alternatively you can run the run.bat file(Note for windows system to run the allure report we need java dependency)


Test execution strategy used :
-----------------------------
 ->  Created 3 test suites for performing sanity test on task_server which contains negative and positive scenarios
 -> The files are test_task_get.py,test_task_post.py,test_task_update.py

Utility details :

 Inside test_task_utility
 -----------------------
  -> config_reader utility is used to read all the config data present inside resources folder
  -> logging script is written for creating logger instance to write logs
  -> task_utility is the bridge between my test class and the rest_client utility
  ->utility_helper is used to construct url and logfile path by reading data from configreader

 Inside client_utility
 ---------------------
  ->request_client is written for call all the HTTP requests and get the responses
  ->request_exception is written for custom exception


Architecture wise all test scripts will interact with task_utility which internally interact with the request_client
and all the exceptions are handled in task_utility.

Please find the sample report in the allure-report/allure-details/bin/allure-report/index.html ,sample report is available

please find the overview report present in test_report/report.html

