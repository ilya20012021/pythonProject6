import subprocess
def cwe():
    subprocess.call("bandit -r D:\pythonProject1 -f json -o D:\i.json",shell = True)