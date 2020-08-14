import pytest
from test_task_utility.config_reader import create_task
from test_task_utility.logging import logger
from test_task_utility.task_utility import TaskUtility


@pytest.fixture(scope="class")
def create_and_get_task():
    TaskUtility().create_task_return_taskid()


@pytest.mark.usefixtures("create_and_get_task")
class TestTaskAPI(TaskUtility):

 """
 This method used to get the task using task id
 """

 def test_get_task(self):
    logger.info('Executing GET Task API')
    logger.info('Sending the get request with task id %s',  TaskUtility.task_id)
    logger.info("Static Variable %s",)
    response = TestTaskAPI().get_task(TaskUtility.task_id)
    logger.info('Got the status  code as %s', response)
    assert response != "", "Get Task API Failed"
    logger.info('Verified created task json %s with get task json %s', create_task, response)
    assert response == create_task, "Create task json is not matched with get task json"


 """
 This method used to get all the task details created in server
 """
 def test_get_multiple_tasks(self):
    response = TestTaskAPI().get_multiple_tasks()
    assert response.status_code==200, "Didn't get the response for all tasks"
