import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/libs")

import time
import json
import GY_VL53L1X
tof = GY_VL53L1X.GY_VL53L1X("/dev/tty.usbserial-A901OBX1")

result_json = {'status': 'NG','distance':-1,'max':-1}
for r in range(0,100):
    d = tof.get_distance()
    if d['distance'] != -1 :
        result_json = {'status': 'OK','distance':d['distance'],'max':d['max']}
        break
    time.sleep(0.3)

print(json.dumps(result_json))

tof.stop_ranging()
