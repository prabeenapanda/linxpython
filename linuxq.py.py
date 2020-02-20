file=open("input.json",'r')
ip=file.read()
import json
import os
d = json.loads(ip)
req = d['Dependencies']
success = []
failure = []
for p in req:
    cmd = f"pip install {p}"
    res = os.system(cmd)
    if  res == 0:
        success.append(p)
    else:
        failure.append(p)
print("Success",success)
print("Failure",failure)
