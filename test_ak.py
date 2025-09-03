import subprocess

def test_script_runs():
    result = subprocess.run(["python3", "simple.py"], capture_output=True, text=True)
    print(result.stdout)
    assert result.returncode == 0, "simple.py failed"
