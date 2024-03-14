#import os
#os.system('python3 exercises/code/python/00_cml.py')
#os.system('python3 exercises/code/python/01_spark.py')

import subprocess
import sys
command = "bash exercises/code/python/run_exercise.sh"

try:
    # Execute the command
    result = subprocess.run(command, shell=True, check=False)

    print(result)
    # Check the return code
    if result.returncode != 0:
        raise Exception(f"Command failed with return code {result.returncode}")
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(result.returncode)
