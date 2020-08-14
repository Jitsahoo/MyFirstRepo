import pytest
from test_task_utility.task_utility import TaskUtility
from test_task_utility.logging import logger
from test_task_utility.config_reader import update_task


@pytest.fixture(scope="class")
def create_and_get_task():
    TaskUtility().create_task_return_taskid()


@pytest.mark.usefixtures("create_and_get_task")
class TestTaskUpdate(TaskUtility):

    """
    This method used to modify the task using taskid
    """
    def test_modify_task(self):
        logger.info("Executing Modify Task API")
        logger.info('Sending the POST request with task id %s', TaskUtility.task_id)
        response = TaskUtility().update_task(TaskUtility.task_id, update_task)
        logger.info("Verify update task json is updated successfully expected %s ,Actual %s", update_task, response)
        assert response == update_task, "Update task api didn't updated the task"

    """
    This method used to delete the task using the task id
    """
    def test_delete_task(self):
        logger.info("Executing Delete Task API")
        logger.info('Sending the Delete request with task id %s', TaskUtility.task_id)
        response = TaskUtility().delete_task(TaskUtility.task_id)
        assert 200 == response.status_code, "Unable to delete the task"
    """
    This method used to get task details using the deleted taskid
    """
    def test_deleted_taskid(self):
        logger.info("Executing GET Task API using deleted task id")
        logger.info('Sending the GET request with task id %s', TaskUtility.task_id)
        TaskUtility().get_task_using_deleted_taskid(TaskUtility.task_id)

    """
    This method used to modify the task using invalid task id
    """
    def test_modify_task_with_invalid(self):
        logger.info("Executing Modify Task API")
        logger.info('Sending the POST request with task id %s', 456)
        TaskUtility().update_task_using_invalid_id(456, update_task)