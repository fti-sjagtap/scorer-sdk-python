# VL53L1X 赤外線測距センサリファレンスボード を USB接続して利用する サンプル
赤外線測距センサ VL53L1X リファレンスボード を SCORER で利用するためのサンプル

## 接続
| Raspberry Pi3 | VL53L1X |
|:------------:|:------------:|
| USB ポート | USB |

## ライブラリ

1. サンプルを実行してみる
```bash
cd ~/scorer-sdk-python/samples/Sensor/VL53L1X_USB/examples
sample.py
```

## サンプル実行方法
1. サンプルへのアクセス
http://xxx.xxx.xxx.xxx:20002/samples/Sensor/VL53L1X_USB/
2. 操作方法
ブラウザ画面に VL53L1X で取得した距離が表示される<br>
![実行した画面]()


## ライブラリサンプル
VL53L1X_USB をシンプルに利用したサンプルコード
```python:sample.py
import sys,os
sys.path.append(os.pardir+"/libs")

import time
import VL53L1X_USB
tof1 = VL53L1X_USB.VL53L1X_USB("/dev/ttyACM0")
#tof2 = VL53L1X_USB.VL53L1X_USB("/dev/ttyACM1")

# Start ranging
for c in range(0,100):
    result1 = tof1.get_distance()
    print(result1)
    #print ("tof1 %d %d mm" % (c, result1['distance']))
    #result2 = tof2.get_distance()
    #print ("tof2 %d %d mm" % (c, result2['distance']))
    time.sleep(0.3)

tof1.stop_ranging()
#tof2.stop_ranging()
```
