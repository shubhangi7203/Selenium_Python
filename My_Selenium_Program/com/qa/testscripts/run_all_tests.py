import pytest
import glob

# Collect all Python test files in current directory
# (excluding this runner file itself)
files = [f for f in glob.glob("*.py") if f != "run_all_tests.py"]

print("\n================ Running Tests with Pytest ================\n")
print(f"Discovered test files: {files}\n")

pytest_args = files + [
    "--junitxml=../../../../result.xml",   # JUnit report (for Jenkins Test Result Trend)
    "--html=../../../../report.html",      # HTML report (human-readable)
    "--self-contained-html"                # Embed CSS/JS inside HTML
]

# Run pytest with the given arguments
exit_code = pytest.main(pytest_args)

print("\n================ Test Execution Completed ================\n")

# Exit with pytest's return code (important for Jenkins build status)
exit(exit_code)
