import pytest
import os

# Reports folder inside Jenkins workspace
report_dir = os.path.join(os.getcwd(), "reports")
os.makedirs(report_dir, exist_ok=True)

exit_code = pytest.main([
    "My_Selenium_Program/com/qa/testscripts",   # Run all tests in this folder
    f"--junitxml={os.path.join(report_dir, 'result.xml')}",
    f"--html={os.path.join(report_dir, 'report.html')}",
    "--self-contained-html"
])

exit(exit_code)
