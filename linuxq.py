import json
import os
try:
    file=open("input.json",'r')
    ip=file.read()
    d = json.loads(ip)
    req = d['Dependencies']
    success = []
    failure = []
    for p in req:
        cmd = f"pip install {p}"
        try:
            res = os.system(cmd)
        except:
            try:
                res = os.system(cmd)
            except:
                try:
                    res = os.system(cmd)
                except:
                    failure.append(p)
        if res == 0:
            success.append(p)
        else:
            failure.append(p)
    print("Success",success)
    print("Failure",failure)
except:
    Print ("Something went wrong")
