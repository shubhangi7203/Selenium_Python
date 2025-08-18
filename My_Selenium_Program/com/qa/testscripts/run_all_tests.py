import os
import glob

# Get all .py files from current directory (excluding run_all_tests.py)
files = [f for f in glob.glob("*.py") if f != "run_all_tests.py"]

pytest_args = [
    files,                            # Run all .py files in this folder
    "--junitxml=../../../../result.xml",    # Save JUnit report (for Jenkins Test Result Trend)
    "--html=../../../../report.html",       # Save HTML report
    "--self-contained-html"                 # Make HTML report standalone (no external CSS/JS)
]

print(f"Running the following files:\n{files}\n")

for file in files:
    print(f"\n=== Running {file} ===")
    os.system(f"python {file}")
