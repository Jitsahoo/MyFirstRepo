import pytest
from test_task_utility.task_utility import TaskUtility
from test_task_utility.logging import logger


@pytest.fixture(scope="class")
def create_and_get_task():
    TaskUtility().create_task_return_taskid()


@pytest.mark.usefixtures("create_and_get_task")
class TestTaskPost(TaskUtility):
    """
    This method used to complete the task using taskid
    """
    def test_complete_task(self):
        logger.info('Executing completed Task API')
        logger.info('Sending the POST request with task id %s', TaskUtility.task_id)
        response = TestTaskPost().get_completed_task(TaskUtility.task_id)
        logger.info("Task status completed %s", response["completed"])
        assert True == response["completed"], "Completed API didn't work as completed is " \
                                              "{complete}".format(response["completed"])

    """
        This method used to incomplete the task using taskid
     """
    def test_incomplete_task(self):
        logger.info('Executing Incomplete Task API')
        logger.info('Sending the POST request with task id %s', TaskUtility.task_id)
        response = TestTaskPost().get_incompleted_task(TaskUtility.task_id)
        logger.info("Task status completed %s", response["completed"])
        assert False == response["completed"], "Completed API didn't work as completed is " \
                                               "{complete}".format(response["completed"])

    """
    This method used to get the 404 as we are giving wrong task id
    """
    def test_incomplete_task_with_invalid_taskid(self):
        logger.info('Executing Incomplete Task API')
        logger.info('Sending the POST request with task id %s', 123)
        TestTaskPost().incomplete_task_using_invalid_id(123)
