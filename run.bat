cd D:\AquaTask\api_test\test_endpoint 
pytest D:\AquaTask\api_test\test_endpoint  --alluredir=../test_report/myreport
cd\
cd D:\AquaTask\task_server_automation\allure-report\allure-details\bin
allure generate --clean D:\AquaTask\api_test\test_report\myreport
pause