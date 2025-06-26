import subprocess
import json

from utils.logger_util import create_logger
from utils.result_logger import log_test_result

# define Paths
report_path="reports/report.html"
json_path="reports/report.json"
testpath="tests/test_login.py"
platform="ios"
# Run pytest
subprocess.run([
    "pytest", # "python3", "-m", "pytest",
    testpath,
    "--platform="+platform,
    "--html="+report_path,
    "--json-report",
    "--json-report-file="+json_path,

])
#Load Test summary from json
with open(json_path,"r") as file:
    data =json.load(file)

summary= data["summary"]
total=summary["total"]
passed=summary.get("passed",0)
failed=summary.get("failed",0)
skipped=summary.get("skipped",0)
if failed==0:
    status="PASSED"
else:
    status="FAILED"

# Log to CSV
log_test_result(status,total,passed,failed,skipped,platform,report_path)
logger = create_logger("Test Runner")
logger.info("Test RUN Complete..")