import subprocess

def test_script_runs():
    result = subprocess.run(["python3", "simple.py"], capture_output=True, text=True)
    print(result.stdout)   # show script output in Jenkins logs
    assert result.returncode == 0, "Script failed with exit code 1"
