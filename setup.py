from setuptools import setup, find_packages

setup(
    name='task_server_automation',
    description='Simple API testing with pytest',
    long_description='validate rest calls for the app deployed in server',
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=['requests','pytest','allure-pytest','allure-python-commons','exception'],
    scripts=['test_task_get.py','test_task_post.py','test_task_update.py']
)