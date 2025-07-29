import os
import glob

# Get all .py files from current directory (excluding run_all_tests.py)
files = [f for f in glob.glob("*.py") if f != "run_all_tests.py"]

print(f"Running the following files:\n{files}\n")

for file in files:
    print(f"\n=== Running {file} ===")
    os.system(f"python {file}")
