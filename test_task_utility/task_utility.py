from client_utility.request_client import Request
from client_utility.request_exception import MyException
from test_task_utility.utility_helper import Helper
import json
from test_task_utility.logging import logger
from test_task_utility.config_reader import create_task


class TaskUtility:

    task_id = ""

    def create_task_return_taskid(self):
        logger.info('Executing create task api')
        logger.info('Sending the POST request %s', Helper.url)
        try:
            response = Request(Helper.url).post_request(json=create_task)
            logger.info('Got the status  code as %s', response.status_code)
            assert 200 == response.status_code, "Create Task API Failed"
        except AssertionError as error:
            logger.error("Create task api didn't work got the error {error}".format(error=error.args[0]))
            raise MyException("Task id not Found so got error code {error_code}".format(error_code=response.status_code))
        json_data = json.loads(response.text)
        logger.info(json_data)
        logger.info('Created Task_id is :: %s', json_data["task_id"])
        TaskUtility.task_id = json_data["task_id"]
        return TaskUtility.task_id

    def get_task(self,taskid):
        try:
            response = Request(Helper.url+"/{task_id}".format(task_id=taskid)).get_request()
            assert 200 == response.status_code, "Unable to get the Task details from the task id {task_id}".format(task_id=taskid)
        except AssertionError as error:
            logger.error("Get task api didn't work as we got the error {error} ".format(error=error.args[0]))
            raise MyException("Task id not Found so got error code {error_code}".format(error_code=response.status_code))

        json_data = json.loads(response.text)
        return json_data


    def get_multiple_tasks(self):
        try:
            response = Request(Helper.url).get_request()
            assert 200 == response.status_code, "Get task api to show all task created didnt work"
        except AssertionError as error:
            logger.error("Get the assertion error as, {error}".format(error=error.args[0]))
            raise MyException("Error:Get all task details api didn't work got status code {status_code}".format(status_code=response.status_code))
        return response

    def get_completed_task(self,taskid):
        try:
           response = Request(Helper.url + "/{task_id}/completed".format(task_id=taskid)).post_request("")
           assert 200 == response.status_code, "Unable to completed the task using the task id {task_id}".format(task_id=taskid)
        except AssertionError  as error:
            logger.error("Got the assertion error for get completed task as, {error}".format(error=error.args[0]))
            raise MyException("Error:Get completed task details api didn't work got status code {status_code}".format(status_code=response.status_code))

        return self.get_task(taskid)

    def get_incompleted_task(self, taskid):
        try:
            response = Request(Helper.url + "/{task_id}/incomplete".format(task_id=taskid)).post_request("")
            assert 200 == response.status_code, "Unable to completed the task using the task id {task_id}".format(task_id=taskid)
        except AssertionError as error:
            logger.error("Got the assertion error for get incompleted task as, {error}".format(error=error.args[0]))
            raise MyException("Unable to incomplete task may be task id is invalid , {0} with error code {1}".format(taskid,response.status_code))
        return self.get_task(taskid)

    def update_task(self,taskid,update_task):
        try:
            response = Request(Helper.url + "/{task_id}".format(task_id=taskid)).put_request(update_task)
            assert 200 == response.status_code, "Unable to updated the task"
        except AssertionError as error:
            logger.error("Getting assertion error while executing updated task api {error}".format(error=error.args[0]))
            raise MyException("Unable to incomplete task may be task id is invalid , {0} with error code {1}".format(taskid,response.status_code))
        return self.get_task(taskid)

    def delete_task(self,taskid):
        try:
            response = Request(Helper.url + "/{task_id}".format(task_id=taskid)).delete_request()
            assert response.status_code == 200, "Delete task api didnt work"
        except AssertionError as error:
            logger.error("Getting assertion error while executing updated task api {error}".format(error=error.args[0]))
            raise MyException("Unable to incomplete task may be task id is invalid , {0} with error code {1}".format(taskid,response.status_code))

        return response

    def update_task_using_invalid_id(self,taskid,update_task):
        try:
            response = Request(Helper.url + "/{task_id}".format(task_id=taskid)).put_request(update_task)
            assert 404 == response.status_code, "able to updated the task using invalid id"
        except AssertionError as error:
            logger.error("Getting assertion error while executing updated task api {error}".format(error=error.args[0]))
            if(response.status_code==200):
             raise MyException("able to update the  task using invalid taskid , {0} with code {1}".format(taskid,response.status_code))
        return response

    def get_task_using_deleted_taskid(self,taskid):
        try:
            response = Request(Helper.url + "/{task_id}".format(task_id=taskid)).delete_request()
            assert response.status_code == 404, "Delete task api didn't work"
        except AssertionError as error:
            logger.error("Getting assertion error while executing updated task api {error}".format(error=error.args[0]))
            if(response.status_code==200):
             raise MyException("able to incomplete task using invalid taskid, {0} with code {1}".format(taskid,response.status_code))

        return response

    def incomplete_task_using_invalid_id(self,taskid):
        try:
            response = Request(Helper.url + "/{task_id}/incomplete".format(task_id=taskid)).post_request("")
            assert 404 == response.status_code, "able to completed the task using the invalid task id {task_id}".format(task_id=taskid)
        except AssertionError as error:
            logger.error("Got the assertion error for get incompleted task as, {error}".format(error=error.args[0]))
            if(response.status_code==200):
             raise MyException("able to incomplete task using invalid task id , {0}  ,with code {1}".format(taskid,response.status_code))
        return response
